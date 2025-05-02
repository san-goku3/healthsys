from rest_framework import serializers
#from . import models 
from base.models import Patients,Doctor,PatientandDoctor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    
class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields='__all__'

class doctorserializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class mappingserializer(serializers.ModelSerializer):
    class Meta:
        model=PatientandDoctor
        fields='__all__'


