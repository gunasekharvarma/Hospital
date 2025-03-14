from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get_details_of_the_patient(request):

    patient_id = request.data.get("patient_id")
    patient_ids_from_query_set = ''
    list_of_patient_ids = list(patient_ids_from_query_set)

    if patient_id in list_of_patient_ids:

        patient = 'Karma'

        response = {
            'Patient Id' : patient,
            'Patient Name' : patient,
            'Patient Email' : patient,
            'Patient Address' : patient,
            'Patient Phone number' : patient,
            'Patient Health Issue' : patient,
            'Patient Last Visited' : patient,
            'Patient Doctor' : patient,
            'Recent Bill' : patient
        }

        return Response(response,status=status.HTTP_200_OK)

    else:
        response = {
            'error' : 'No Patient Details, Please Register'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)


@api_view(['UPDATE'])
def update_details_of_the_patient(request):
    pass