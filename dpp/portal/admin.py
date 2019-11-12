from django.contrib import admin
from .models import Person, Doctor, Patient, Appointment,FreeTimings

# Register your models here.
admin.site.register(Person)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(FreeTimings)
