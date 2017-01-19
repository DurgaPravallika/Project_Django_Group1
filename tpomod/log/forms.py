#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class FilterForm(forms.Form):
    Percentage = forms.FloatField( label = "Percentage:")
    Backlogs = forms.IntegerField( label = "Backlogs:")
    wise = forms.BooleanField(label = "WISE:",required=False)
    mrnd = forms.BooleanField(label = "MRND:",required=False)
    atl = forms.BooleanField(label = "ATL:",required=False)
    iot = forms.BooleanField(label = "IOT:",required=False)

