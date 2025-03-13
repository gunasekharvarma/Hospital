from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def login_view(request):
    pass

@api_view(['POST'])
def create_patient_id(request):
    name = request.data.get("name")
    phone_number = request.data.get("phone_number")
    
