#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
from log.models import StudentInfo
from log.models import StudentInfo

@login_required(login_url="login/")
def home(request):
   #return render(request,"home.html")
   data = StudentInfo.objects.count()
   mrnd = StudentInfo.objects.filter(mrnd=1).count()
   wise = StudentInfo.objects.filter(wise=1).count()
   atl = StudentInfo.objects.filter(atl=1).count()
   iot = StudentInfo.objects.filter(iot=1).count()
   print data
   return TemplateResponse(request,"home.html",{"data": data,"wise":wise,"mrnd":mrnd,"atl":atl,"iot":iot})	

@login_required(login_url="login/")
def students(request):
   #return render(request,"home.html")
   studs = StudentInfo.objects.all()
   print studs
   return TemplateResponse(request,"students.html",{"studs": studs})	
	