from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CustomForm,DoctorProfileForm,SearchDoctorForm,PatientProfileForm
from .models import Person, Patient, Doctor
from django.db import connection
from django.contrib import messages
# Create your views here.

def homeview(request):
    user=request.user
    if(user.is_authenticated and not (user.is_staff) ):
        cursor=connection.cursor()
        cursor.execute('select * from portal_person WHERE user_id= %s',[user.id])
        person=cursor.fetchone()
        # cursor.execute('select * from portal_appointment where 
        #print(person)
        return render(request, 'portal/home.html', {'person':person})
    return render(request,'portal/home.html',{})

def register(request):
    if(request.method == 'POST'):
        form = CustomForm(request.POST)
        if(form.is_valid()):
            cursor=connection.cursor()
            form.save()
            occupation=form.cleaned_data.get('occupation')
            email=form.cleaned_data.get('email')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            messages.success(request, f"New account created: {username}")
            cursor.execute('Select id from auth_user where username=%s',[username])
            userid = cursor.fetchone()
            cursor.execute('INSERT INTO portal_person (user_id,username,email,occupation) values (%s,%s,%s,%s)',[userid[0],username,email,occupation])
            if(occupation == 'doctor'):
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_doctor (username,email,user_id) values (%s,%s,%s)',[username,email,userid[0]])
            else:
                cursor=connection.cursor()
                cursor.execute('INSERT INTO portal_patient (username,email,user_id) values (%s,%s,%s)',[username,email,userid[0]])
            user=authenticate(username=username,password=password)
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            cursor.execute('select * from portal_person where user_id= %s',[user.id])
            person=cursor.fetchone()
            return redirect('homepage')
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
                cursor.execute('select * from portal_person WHERE user_id= %s',[user.id])
                person=cursor.fetchone()
                print(person)
                if(person[2]=="doctor"):
                    cursor.execute('select * from portal_appointment a where a.did_id in (select id from portal_doctor where username= %s )',[username])
                else:
                    cursor.execute('select * from portal_appointment a where a.pid_id in (select id from portal_patient where username= %s )',[username])
                appointments=cursor.fetchall()
                return redirect('homepage')
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
    
    if(request.method=="GET"):
        form=SearchDoctorForm(request.GET)
        if(form.is_valid()):
            user=request.user
            specialization=request.GET.get('specialization')
            cursor=connection.cursor()
            cursor.execute('select * from portal_doctor d inner join portal_freetimings f on d.id=f.did_id where d.specialization=%s',[specialization])
            doctors=cursor.fetchall()
            if(len(doctors)==0):
                numdoctors=0
            else:
                numdoctors=len(doctors)
            print(numdoctors)
            return render(request,'portal/selectdoctor.html',{'doctor_list':doctors,'range':range(24),'numdoctors':numdoctors})

    return render(request,'portal/searchdoctor.html',{'form':form})

def profileeditdoctor(request):
    
    if(request.method=="GET"):
        form=DoctorProfileForm(request.GET)
        if(form.is_valid()):
            user=request.user
            specialization=request.GET.get('specialization')
            name=request.GET.get('name')
            address=request.GET.get('address')
            phone_number=request.GET.get('phone_number')
            tslots=[]
            for i in range(24):
                t='t'+str(i)
                ch=request.GET.get(t)
                if(ch=="on"):
                    tslots.append(1)
                else:
                    tslots.append(0)
            print(tslots)
            cursor=connection.cursor()
            person=get_person_details(user.id)
            cursor.execute('update portal_doctor set specialization= %s,name= %s,address=%s,phone_number=%s where username=%s',[specialization,name,address,phone_number,user.username])
            cursor.execute('update portal_freetimings set t0_1=%s,t1_2=%s,t2_3=%s,t3_4=%s,t4_5=%s,t5_6=%s,t6_7=%s,t7_8=%s,t8_9=%s,t9_10=%s,t10_11=%s,t11_12=%s,t12_13=%s,t13_14=%s,t14_15=%s,t15_16=%s,t16_17=%s,t17_18=%s,t18_19=%s,t19_20=%s,t20_21=%s,t21_22=%s,t22_23=%s,t23_24=%s where did_id=(select id from portal_doctor where username=%s)',[tslots[0],tslots[1],tslots[2],tslots[3],tslots[4],tslots[5],tslots[6],tslots[7],tslots[8],tslots[9],tslots[10],tslots[11],tslots[12],tslots[13],tslots[14],tslots[15],tslots[16],tslots[17],tslots[18],tslots[19],tslots[20],tslots[21],tslots[22],tslots[23],user.username])
            print(person)
            return redirect('homepage')
    else:
        form=DoctorProfileForm()
    return render(request,"portal/editdoctorprofile.html",{'form':form})

def profileeditpatient(request):
    
    if(request.method=="GET"):
        form=PatientProfileForm(request.GET)
        if(form.is_valid()):
            user=request.user
            name=request.GET.get('name')
            address=request.GET.get('address')
            phone_number=request.GET.get('phone_number')
            cursor=connection.cursor()
            person=get_person_details(user.id)
            cursor.execute('update portal_patient set name= %s,address=%s,phone_number=%s where username=%s',[name,address,phone_number,user.username])
            print(person)
            return redirect('homepage')
    else:
        form=PatientProfileForm()
    return render(request,"portal/editpatientprofile.html",{'form':form})

def get_person_details(username):
    cursor=connection.cursor()
    cursor.execute('select * from portal_person WHERE user_id= %s',[username])
    person=cursor.fetchone()
    return(person)

def addapointment(request):
    user=request.user
    x = request.GET.get('id')
    did,tme=map(int,x.split("-"))
    tme="t"+str(tme)+"_"+str(tme+1)
    cursor=connection.cursor()
    cursor.execute('select id from portal_patient where user_id=%s',[user.id])
    pid=cursor.fetchone()
    s='update portal_freetimings set '+tme+"=0 where did_id="+str(did)
    cursor.execute(s)
    cursor.execute('insert into portal_appointment (did_id,pid_id) values (%s,%s)',[did,pid[0]])
    messages.info(request, f"Appointment booked.")
    #print(id)
    return redirect('homepage')

                