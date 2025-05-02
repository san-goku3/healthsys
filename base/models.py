from django.db import models
#from django.contrib.auth.models import AbstractUser


# Create your models here.
'''
class User(AbstractUser):
    pass
'''    

class Patients(models.Model):
    name=models.CharField(max_length=256)
    age=models.IntegerField()
    disease = models.TextField()

class Doctor(models.Model):
    name=models.CharField(max_length=256)
    specia=models.CharField(max_length=256)

class PatientandDoctor(models.Model):
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
