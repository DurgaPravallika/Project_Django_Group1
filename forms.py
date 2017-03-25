from django.forms import ModelForm
from .models import AcademicInfo
#from django.utils import timezone
#from django import forms

class AcademicInfoForm(ModelForm):
    class Meta:
        model = AcademicInfo
        fields = "__all__"