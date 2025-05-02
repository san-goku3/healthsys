from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

from base.models import Patients,Doctor,PatientandDoctor
from base.api.serializers import registerserializer, patientserializer,doctorserializer,mappingserializer
 

#register
@api_view(['POST'])
def register_user(request):
    serializer=registerserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# Example protected view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}! This is a protected view."})


#patients
@api_view(['GET','POST'])
def all_patients(request):
    if request.method=='GET':
        patients=Patients.objects.all()
        serializer=patientserializer(patients,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=patientserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def one_patient(request,pk):
    try:
        selected_patient=Patients.objects.get(pk=pk)
    except Patients.DoesNotExist:
        return Response({'error': 'Patient not found'})
    
    if request.method=='GET':
        serializer=patientserializer(selected_patient)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=patientserializer(selected_patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        selected_patient.delete()
        return Response({'message': 'Patient deleted'})
    

#doctors
@api_view(['GET','POST'])
def all_doctors(request):
    if request.method=='GET':    
        doctors=Doctor.objects.all()
        serializer=doctorserializer(doctors,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=doctorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def one_doctor(request,pk):
    try:
        selected_doctor=Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'})
    
    if request.method=='GET':
        serializer=doctorserializer(selected_doctor)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=doctorserializer(selected_doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        selected_doctor.delete()
        return Response({'message': 'Doctor deleted'})
    

#patient_mapping_with_doctor
@api_view(['GET','POST'])
def all_mapping(request):
    if request.method=='GET':    
        Map=PatientandDoctor.objects.all()
        serializer=mappingserializer(Map,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=mappingserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def one_map(request,pk):
    try:
        selected_Map=PatientandDoctor.objects.get(pk=pk)
    except PatientandDoctor.DoesNotExist:
        return Response({'error': 'Patient not found'})
    
    if request.method=='GET':
        serializer=mappingserializer(selected_Map)
        return Response(serializer.data)

    elif request.method=='DELETE':
        selected_Map.delete()
        return Response({'message': 'Map deleted'})

'''
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

'''

'''
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        'api/token/refresh',
    ]
    return Response(routes)

def getData(request):
    person={"n":"abc","a":"21"}
    return Response(person)

    
'''

