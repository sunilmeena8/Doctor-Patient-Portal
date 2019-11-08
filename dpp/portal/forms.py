from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomForm(UserCreationForm):
	Choices=[('doctor','doctor'),('patient','patient')]
	occupation=forms.CharField(max_length=20)
	class Meta:
		model=User
		fields=('username','occupation','password1','password2')
	def sav(self,commit=True):
		user=super(CustomForm,self).save(commit=False)
		user.occupation=self.cleaned_data['occupation']
		if commit:
			user.save()
		return user
class DoctorSelectForm(forms.Form):
	Choices=[('c1','c1'),('c2','c2')]
	doctor=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)