
from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class PersonalInfo(models.Model):
   rollno = models.CharField(max_length=200)
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)
   phonenumber = models.CharField(max_length = 10)     
   email = models.CharField(max_length = 100)
   dob = models.CharField(max_length = 15)

class AcademicInfo(models.Model):
    Branch = models.CharField(max_length=100)
    Aggregate = models.CharField(max_length=200)
    YearOfJoin = models.IntegerField()
    SecPecentage = models.FloatField(max_length=200)
    higherSecPer =models.CharField(max_length=200)
    Backlogs=models.CharField(max_length=10)

class AdditionalInfo(models.Model):
    Internships = models.CharField(max_length=100)
    Certificates = models.CharField(max_length=200)
    Extra = models.CharField(max_length=200)
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Notification(models.Model):
    #notid = models.ForeignKey(PersonalInfo)
    Date = models.IntegerField(default=0)
    Stuid =  models.IntegerField(default=0)
    From = models.CharField(max_length=100, null=False)
    Dept = models.CharField(max_length=100, null=False)
    Notify = models.IntegerField(default=0)

    
# Create your models here.
