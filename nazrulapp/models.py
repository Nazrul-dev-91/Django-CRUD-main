from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    phone = models.IntegerField(null=True,blank=True)
    nid = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.username
    
class DoctorModel(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class PatientModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
   
    