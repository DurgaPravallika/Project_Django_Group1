from django.shortcuts import render
from .models import StudentDetails
def index(request):
    details = StudentDetails.objects.all()
    return render(request, 'sample/index.html', {'details': details})
