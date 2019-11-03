from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomForm(UserCreationForm):
	occupation=forms.CharField(max_length=200)
	class Meta:
		model=User
		fields=('username','occupation','password1','password2')
