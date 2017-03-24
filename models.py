from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class RegistrationModel(models.Model):
 
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length = 100)
    
    

def _str_(self):
    return self.rollno
