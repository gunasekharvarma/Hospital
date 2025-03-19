from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import *


# Create your views here.
def login(request):
    return render(request,'accounts/index.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

@api_view(['POST'])
def staff_login(request):
    try:

        username = request.data.get("username")
        password = request.data.get("password")
        auth_user = authenticate(request, username=username, password=password)
        user = User.objects.get(username = username)

        if not hasattr(user, "staff"):
            return Response({"error": "User is not a staff member"}, status=403)

        if User.objects.filter(username=username).exists() and auth_user:

            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)

            response = {
                'message': "Login Successful",

                'token': token.key
            }

            return Response(response, status=200)

        else:
            return Response({'error': "Invalid Credentials"}, status=200)



    except Exception as e:
        return Response({'error1': "Invalid Credentials"}, status=200)


@api_view(['POST'])
def staff_logout(request):
    try:

        token_generated = request.data.get("token_generated")
        token = Token.objects.get(key = token_generated)
        token.delete()

        response = {
            'message':'User Successfully Logged Out'
        }
        return Response(response,status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            'error':'Error in Logout'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_details_of_the_staff(request):

    username = request.data.get("username")
    usernames_from_query_set = User.objects.values_list('username',flat=True)
    list_of_usernames = list(usernames_from_query_set)

    if username in list_of_usernames:

        user = User.objects.get(username=username)

        response = {
            'username' : user.username,
            'role':user.staff.role,
            'first_name':user.first_name
        }

        return Response(response,status=status.HTTP_200_OK)

    else:

        response = {
            'message': 'User Not Available'
        }

        return Response(response,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_patient_id(request):
    name = request.data.get("name")
    phone_number = request.data.get("phone_number")
    age = request.data.get("age")


@api_view(['POST'])
def create_a_new_staff(request):
    password = request.data.get("password")
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    is_staff = request.data.get("is_staff")
    is_active = request.data.get("is_active")
    role = request.data.get("role")

    user = User.objects.create_user(password=password,username=username,first_name=first_name,last_name=last_name,email=email,is_staff=is_staff,is_active=is_active)
    staff = Staff(user=user,role=role)
    staff.save()

    return Response({"message":"Staff Created"},status = status.HTTP_201_CREATED)
