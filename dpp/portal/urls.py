"""dpp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='homepage'),
    path('register/',views.register),
    path('login/',views.login_req),
    path('logout/',views.logout_req),
    path('searchdoctor/searchbyspecialization/',views.doctor_search_by_specialization,name='searchfordoctor'),
    path('searchdoctor/searchbyusername/',views.doctor_search_by_username),
    path('searchdoctor/',views.doctor_search_by),
    path('editprofiledoctor/',views.profileeditdoctor,name='editdoctor'),
    path('selectdoctor/',views.addapointment),
    path('editprofilepatient/',views.profileeditpatient,name='editpatient'),
    path('cancelappointment/',views.cancelAppointment),
    path('appointmenthistory/',views.appointmenthistory),
    path('doneappointment/',views.doneappointment),
    path('myaccount/',views.myaccount),
]
