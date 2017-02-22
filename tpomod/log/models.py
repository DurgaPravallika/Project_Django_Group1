
from django.db import models
from django.contrib.auth.models import User

class StudentInfo(models.Model):
   username = models.CharField(max_length=100)
   percentage = models.IntegerField()
   name = models.CharField(max_length=150)
   backlogs = models.IntegerField()
   wise = models.IntegerField(default = 0)
   atl = models.IntegerField(default = 0)
   mrnd = models.IntegerField(default = 0)
   iot = models.IntegerField(default = 0)
    
	