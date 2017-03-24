from django.db import models


class AcademicInfo(models.Model):
	Branch = models.CharField(max_length=100)
	Aggregate = models.CharField(max_length=200)
	YearOfJoin = models.IntegerField()
	SecPecentage = models.FloatField(max_length=200)
	higherSecPer =models.CharField(max_length=200)
	Backlogs=models.CharField(max_length=10)
	
