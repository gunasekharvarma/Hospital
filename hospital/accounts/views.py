from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import *


# Create your views here.

@api_view(['POST'])
def staff_login(request):

    try:

        username = request.data.get("username")
        password = request.data.get("password")

        usernames_from_query_set = StaffUser.objects.values_list('username', flat=True)
        list_of_usernames = list(usernames_from_query_set)

        passwords_from_query_set = StaffUser.objects.values_list('password', flat=True)
        list_of_passwords = list(passwords_from_query_set)

        #auth_staff = authenticate(request,username=username,password=password)

        if (username in list_of_usernames) and (password in list_of_passwords):

            #user = auth_staff
            user = StaffUser.objects.get(username=username)

            token= Token.objects.create(user=user)

            response = {
                'message': 'User Successfully Logged In',
                'token': token.key
            }

            return Response(response, status=status.HTTP_200_OK)

        else:

            response = {
                'message': 'Invalid Credentials'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        response = {
            'error' : 'Error in Login'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)


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
    usernames_from_query_set = StaffUser.objects.values_list('username',flat=True)
    list_of_usernames = list(usernames_from_query_set)

    if username in list_of_usernames:

        staff = StaffUser.objects.get(username=username)

        response = {
            'username' : staff.username,
            'role':staff.role,
            'first_name':staff.first_name
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

    staff = StaffUser(password=password,username=username,first_name=first_name,last_name=last_name,email=email,is_staff=is_staff,is_active=is_active,role=role)
    staff.save()

    return Response({"message":"Staff Created"},status = status.HTTP_201_CREATED)
