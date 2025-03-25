from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('details/<int:phone_number>/',get_details_of_the_patient,name="details"),
    path('create/',create_patient,name="Create a new patient"),
    path('update/',update_details_of_the_patient,name="Update the details of the patient"),
    path('renderupdate',update,name="update"),
    path('rendercreate',create,name='create')
]