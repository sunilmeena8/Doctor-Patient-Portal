from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import CustomForm
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
			user=authenticate(username=username,password=password)
			login(request,user)
			return render(request,'portal/home.html')
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
			return render(request,'portal/home.html')
	else:
		form=AuthenticationForm()
	return render(request,'portal/login.html',{'form':form})

def logout_req(request):
	logout(request)
	return render(request,"portal/home.html")