from django.db import models

# Create your models here.
class Person(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=20)
	occupation=models.CharField(max_length=20)

class Doctor(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=20)
	
class Patient(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=20)