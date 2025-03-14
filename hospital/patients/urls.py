from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('details/',get_details_of_the_patient,name="Details of the patient")
]