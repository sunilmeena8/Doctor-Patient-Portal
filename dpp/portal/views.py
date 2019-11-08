from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CustomForm,DoctorSelectForm
from .models import Person, Patient, Doctor
from django.db import connection
from django.contrib import messages
# Create your views here.


def homeview(request):
    user=request.user
    if(user.is_authenticated and not (user.is_staff) ):
        cursor=connection.cursor()
        cursor.execute('select * from portal_person WHERE name= %s',[user.username])
        person=cursor.fetchone()
        return render(request, 'portal/home.html', {'person':person})
    return render(request,'portal/home.html',{})


def register(request):
    if(request.method == 'POST'):
        form = CustomForm(request.POST)
        if(form.is_valid()):
            '''cursor=connection.cursor()
            cursor.execute('select * from auth_user where username= %s',[form.cleaned_data.get('username')])
            aluser=cursor.fetchone()
            print(aluser)
            if(len(aluser)>=1):
                messages.error(request,"Username already taken.")'''
            user=form.sav()
            username = user.username
            occupation = user.occupation
            messages.success(request, f"New account created: {username}")
            cursor.execute('INSERT INTO portal_person (name,occupation) values (%s,%s)',[username,occupation])
            if(occupation == 'doctor'):
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_doctor ("name") values (%s)',[username])
            else:
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_patient ("name") values (%s)',[username])
            #user=authenticate(username=username,password=password)
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            cursor.execute('select * from portal_person where name= %s',[username])
            person=cursor.fetchone()
            return render(request, 'portal/home.html', {'person': person})
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "portal/register.html",
                          context={"form":form})
    else:
        form = CustomForm()
    return render(request, 'portal/register.html', {'form': form})


def login_req(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(request, data=request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                cursor=connection.cursor()
                cursor.execute('select * from portal_person WHERE name= %s',[username])
                person=cursor.fetchone()
                print(person)
                if(person[2]=="doctor"):
                    cursor.execute('select * from portal_appointment a where a.did in (select id from portal_doctor where name= %s )',[username])
                else:
                    cursor.execute('select * from portal_appointment a where a.pid in (select id from portal_patient where name= %s )',[username])
                appointments=cursor.fetchall()
                return render(request, 'portal/home.html', {'person': person,'appointments':appointments})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})


def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('homepage')

def doctor_search(request):
    #doctors=Doctor.objects.raw('select * from portal_doctor')
    form=DoctorSelectForm
    
    cursor=connection.cursor()
    cursor.execute('select * from portal_doctor')
    doctors=cursor.fetchall()
    # print(doctors)
    return render(request,'portal/searchdoctor.html',{'doctor_list':doctors,'form':form})

def appoint(request,doctor):
    print(doctor)
    return HttpResponse(request,"Hi")