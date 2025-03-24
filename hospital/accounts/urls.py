from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',login,name="login"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('login/',staff_login,name="loginstaff"),
    path('logout/',staff_logout,name="logout"),
    path('createstaff/',create_a_new_staff,name="Create a new Staff"),
    path('details/',get_details_of_the_staff,name="Details of the staff")
]