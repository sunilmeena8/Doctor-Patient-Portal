from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import CustomForm
from .models import Person,Patient,Doctor
# Create your views here.
def homeview(request):
    return render(request , 'portal/home.html' , {})

def register(request):
	if(request.method=='POST'):
		form=CustomForm(request.POST)
		if(form.is_valid()):
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			occupation=form.cleaned_data.get('occupation')
			person=Person()
			person.name=username
			person.occupation=occupation
			person.save()
			if(occupation=='doctor'):
				doctor=Doctor()
				doctor.name=username
				doctor.save()

			else:
				patient=Patient()
				patient.name=username
				patient.save()
			user=authenticate(username=username,password=password)
			login(request,user)
			return render(request,'portal/home.html',{'person':person})
		else:
			pass
	else:
		form=CustomForm()
	return render(request,'portal/register.html',{'form':form})

def login_req(request):
	if(request.method=='POST'):
		form=AuthenticationForm(request,data=request.POST)
		if(form.is_valid()):
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user= authenticate(username=username,password=password)
			login(request,user)
			person=Person()
			for i in Person.objects.all():
				if(i.name==username):
					person=i
					break
			return render(request,'portal/home.html',{'person':person})
			
			
	else:
		form=AuthenticationForm()
	return render(request,'portal/login.html',{'form':form})

def logout_req(request):
	logout(request)
	return render(request,"portal/home.html")