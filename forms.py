from django.forms import ModelForm
from StudentInfo.models import AdditionalInfo
#from django.utils import timezone
#from django import forms

class AdditionalInfoForm(ModelForm):
	class Meta:
		model = AdditionalInfo
		fields = "__all__"

