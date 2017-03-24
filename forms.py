'''from django.forms import ModelForm

from .models import AcademicInfo

class AcademicInfoForm(ModelForm):
	class Meta:
		model = AcademicInfo
		fields = "__all__"
'''
from django.forms import ModelForm
from myapp.models import AcademicInfo
#from django.utils import timezone
#from django import forms

class AcademicInfoForm(ModelForm):
	class Meta:
		model = AcademicInfo
		fields = "__all__"

