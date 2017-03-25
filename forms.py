#from django import forms
from django.forms import ModelForm
from .models import Registration
from .models import PersonalInfo
from .models import AcademicInfo
from .models import AdditionalInfo
from .models import Login
#from django.utils import timezone
#from django import forms

class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

class LogForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class PerForm(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = "__all__"

class AcadForm(ModelForm):
    class Meta:
        model = AcademicInfo
        fields = "__all__"

class AddForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = "__all__"


