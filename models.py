from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
# Create your models here.
class StudentDetails(models.Model):
   rollno = models.CharField(max_length=200)
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)

   phonenumber = models.CharField(max_length = 10)     
   email = models.CharField(max_length = 100)
   dob = models.CharField(max_length = 15)
   def _str_(self):
       return self.rollno

