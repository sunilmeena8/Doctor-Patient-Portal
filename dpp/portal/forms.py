from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomForm(UserCreationForm):
	Choices=[('doctor','doctor'),('patient','patient')]
	occupation=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
	email=forms.CharField(max_length=40)
	class Meta:
		model=User
		fields=('username','email','occupation','password1')
	

class DoctorProfileForm(forms.Form):
	Choices=[('heart','heart'),('eye','eye'),('brain','brain'),('lungs','lungs'),('other','other')]

	specialization=forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
	name=forms.CharField(max_length=50)
	phone_number=forms.CharField(max_length=50)
	address=forms.CharField(max_length=100)
	t0=forms.BooleanField(required=False)
	t1=forms.BooleanField(required=False)
	t2=forms.BooleanField(required=False)
	t3=forms.BooleanField(required=False)
	t4=forms.BooleanField(required=False)
	t5=forms.BooleanField(required=False)
	t6=forms.BooleanField(required=False)
	t7=forms.BooleanField(required=False)
	t8=forms.BooleanField(required=False)
	t9=forms.BooleanField(required=False)
	t10=forms.BooleanField(required=False)
	t11=forms.BooleanField(required=False)
	t12=forms.BooleanField(required=False)
	t13=forms.BooleanField(required=False)
	t14=forms.BooleanField(required=False)
	t15=forms.BooleanField(required=False)
	t16=forms.BooleanField(required=False)
	t17=forms.BooleanField(required=False)
	t18=forms.BooleanField(required=False)
	t19=forms.BooleanField(required=False)
	t20=forms.BooleanField(required=False)
	t21=forms.BooleanField(required=False)
	t22=forms.BooleanField(required=False)
	t23=forms.BooleanField(required=False)
	
class PatientProfileForm(forms.Form):
	name=forms.CharField(max_length=30)
	phone_number=forms.CharField(max_length=50)
	address=forms.CharField(max_length=100)

class SearchDoctorSpForm(forms.Form):	
	Choices=[('heart','heart'),('eye','eye'),('brain','brain'),('lungs','lungs'),('other','other')]
	specialization=forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)
	
class SearchDoctorUnForm(forms.Form):
	username=forms.CharField(max_length=50)
	
