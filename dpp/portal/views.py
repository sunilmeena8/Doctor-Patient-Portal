from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CustomForm
from .models import Person, Patient, Doctor
from django.db import connection
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
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            occupation = form.cleaned_data.get('occupation')
            cursor=connection.cursor()
            cursor.execute('INSERT INTO portal_person (name,occupation) values (%s,%s)',[username,occupation])
            if(occupation == 'doctor'):
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_doctor ("name") values (%s)',[username])
            else:
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_patient ("name") values (%s)',[username])
            user = authenticate(username=username, password=password)
            login(request, user)
            cursor.execute('select * from portal_person where name= %s',[username])
            person=cursor.fetchone()
            return render(request, 'portal/home.html', {'person': person})
        else:
            pass
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
            login(request, user)
            
            
            cursor=connection.cursor()
            cursor.execute('select * from portal_person WHERE name= %s',[username])
            person=cursor.fetchone()
            # print(person)
            return render(request, 'portal/home.html', {'person': person})

    else:
        form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})


def logout_req(request):
    logout(request)
    return redirect('homepage')

def doctor_search(request):
    #doctors=Doctor.objects.raw('select * from portal_doctor')
    cursor=connection.cursor()
    cursor.execute('select * from portal_doctor')
    doctors=cursor.fetchall()
    # print(doctors)
    return render(request,'portal/searchdoctor.html',{'doctor_list':doctors})