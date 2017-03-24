from django.db import models

# Create your models here.
class AdditionalInfo(models.Model):
	Activities = models.CharField(max_length=255)
	Certificates =  models.CharField(max_length=255)
	Internships = models.CharField(max_length=255)
	Projects = models.CharField(max_length=255)