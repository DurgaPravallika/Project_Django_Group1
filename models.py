from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
# Create your models here.
class PersonalInfo(models.Model):
   rollno = models.CharField(max_length=200)
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)
   phonenumber = models.CharField(max_length = 10)     
   email = models.CharField(max_length = 100)
   dob = models.CharField(max_length = 15)
 class AcademicInfo(models.Model):
    rollno = models.ForeignKey('PersonalInfo.rollno')
    yearofjoin = models.IntegerField(default=0, null=False)
    agg = models.FloatField(default=0, null=False)
    interclg = models.CharField(max_length=200, null=False)
    interagg = models.FloatField(max_length=200, null=False)
    ssc = models.CharField(max_length=200, null=False)
    sscagg = models.FloatField(default=0, null=False)
 class AdditionalInfo(models.Model):
       rollno = models.ForeignKey('PersonalInfo.rollno')
       internships = models.CharField(max_length=200)
       Activities = models.CharField(max_length=200)
       projects = models.CharField(max_length=200)
       Certificates = models.CharField(max_length=200)
     
   def _str_(self):
       return self.rollno