from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from datetime import datetime

from .models import *
from django.shortcuts import render

# Create your views here.

def update(request):
     return render(request,'accounts/update.html')


def create(request):
    return render(request,'accounts/create.html')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_details_of_the_patient(request,phone_number):

    if not hasattr(request.user,"staff"):
        return Response({'message':'Login Required'})

    else:

        if phone_number:

            patient = Patients.objects.get(phone_number=phone_number)
            

            response = {
                'Patient_Id' : patient.id,
                'Patient_FirstName' : patient.first_name,
                'Patient_LastName': patient.last_name,
                'Patient_Age': patient.age,
                'Patient_Email' : patient.email,
                'Patient_BloodGroup':patient.blood_group,
                'Patient_Phonenumber' : patient.phone_number,
                'Patient_HealthIssue' : patient.medical_issue,
                'Patient_Medication' : patient.medication,
                'Patient_LastVisited' : patient.last_visited,
                'Patient_Doctor' : patient.assigned_doctor,
                'Recent_Bill' : patient.recent_bill,
                'Updated_By' : patient.updated_by.username
            }

            return Response(response,status=status.HTTP_200_OK)

        else:
            response = {
                'error' : 'No Patient Details, Please Register'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_details_of_the_patient(request):
    try:
        phone_number = request.data.get("phone_number")
        blood_group = request.data.get("blood_group")
        medical_issue = request.data.get("medical_issue")
        medication = request.data.get("medication")
        recent_bill = request.data.get("recent_bill")

    except Exception as e:
            response = {
                'message' : 'User Not Found'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

    if not hasattr(request.user,"staff"):
        return Response({
            'Message' : "Only Staff Logged In members can update the data"
        })
    patient = Patients.objects.filter(phone_number = phone_number).update(
            blood_group = blood_group,
            medical_issue = medical_issue,
            medication = medication,
            recent_bill = recent_bill,
            updated_by = request.user.id
            )
    
    

    #updated_fields = []

    # if "blood_group" in data and data["blood_group"]:
    #     patient.blood_group = data["blood_group"]
    #     updated_fields.append("blood_group")

    # if "medical_issue" in data and data["medical_issue"]:
    #     patient.medical_issue = data["medical_issue"]
    #     updated_fields.append("medical_issue")

    # if "medication" in data and data["medication"]:
    #     patient.medication = data["medication"]
    #     updated_fields.append("medication")

    # if "recent_bill" in data and data["recent_bill"]:
    #     patient.recent_bill = data["recent_bill"]
    #     updated_fields.append("recent_bill")

    

    # if updated_fields:

    #     patient.updated_by = request.user
    #     patient.last_visited = datetime.now()
    #     patient.save()

    response = {
        'message' : 'Patient Updated Sucessfully',
        #"Updated By" : request.user.username
    }

    return Response(response,status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_patient(request):
    phone_number = request.data.get("phone_number")
    email = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    age = request.data.get("age")

    phone_numbers = Patients.objects.values_list('phone_number',flat=True)
    list_of_phone_numbers = list(phone_numbers)

    if phone_number in list_of_phone_numbers:

         response = {
             'message' : 'Mobile number Already Registered'
         }

         return Response(response,status=status.HTTP_200_OK)
    else:
        user = User.objects.get()
        patient = Patients(id = uuid.uuid4(),phone_number=phone_number,email=email,first_name=first_name,last_name=last_name,age=age)
        patient.updated_by = request.user
        patient.save()

        #patient = Patients.objects.get(phone_number=phone_number)

        response = {
            'message' : 'Patient is Successfully Created',
            'patient_id' : patient.id,
            'Updated By' : patient.updated_by
        }

        return Response(response,status=status.HTTP_200_OK)





