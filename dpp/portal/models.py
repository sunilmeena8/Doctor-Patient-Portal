from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	username=models.CharField(max_length=40)
	occupation=models.CharField(max_length=20)
	email=models.CharField(max_length=40)

class Doctor(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	username=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	specialization=models.CharField(max_length=40,null=True)
	name=models.CharField(max_length=40,null=True)
	phone_number=models.CharField(max_length=20,null=True)
	address=models.CharField(max_length=100,null=True)
	
class Patient(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	username=models.CharField(max_length=20)
	email=models.CharField(max_length=40)
	name=models.CharField(max_length=40,null=True)
	phone_number=models.CharField(max_length=20,null=True)
	address=models.CharField(max_length=100,null=True)

class Appointment(models.Model):
	
	did=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	pid=models.ForeignKey(Patient,on_delete=models.CASCADE)
	time=models.CharField(max_length=10)
	
class FreeTimings(models.Model):
	
	did=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	t0_1=models.BooleanField()
	t1_2=models.BooleanField()
	t2_3=models.BooleanField()
	t3_4=models.BooleanField()
	t4_5=models.BooleanField()
	t5_6=models.BooleanField()
	t6_7=models.BooleanField()
	t7_8=models.BooleanField()
	t8_9=models.BooleanField()
	t9_10=models.BooleanField()
	t10_11=models.BooleanField()
	t11_12=models.BooleanField()
	t12_13=models.BooleanField()
	t13_14=models.BooleanField()
	t14_15=models.BooleanField()
	t15_16=models.BooleanField()
	t16_17=models.BooleanField()
	t17_18=models.BooleanField()
	t18_19=models.BooleanField()
	t19_20=models.BooleanField()
	t20_21=models.BooleanField()
	t21_22=models.BooleanField()
	t22_23=models.BooleanField()
	t23_24=models.BooleanField()

class AppointmentHistory(models.Model):
	did=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	pid=models.ForeignKey(Patient,on_delete=models.CASCADE)
	time=models.CharField(max_length=10)
