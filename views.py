from django.shortcuts import render,redirect
from .forms import RegForm
from .forms import PerForm
from .forms import AcadForm
from .forms import AddForm
from .forms import LogForm
from .models import Registration
from .models import PersonalInfo
from .models import AcademicInfo
from .models import AdditionalInfo
from .models import Login

def register(request):

    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            Registration = form.save(commit = False)
            Registration.save()
            return redirect('perInfo')
    else:
        form = RegForm
    return render(request, 'registration.html', {'form':form()})

def perInfo(request):

    if request.method == 'POST':
        form = PerForm(request.POST)
        if form.is_valid():
            PersonalInfo = form.save(commit = False)
            PersonalInfo.save()
            return redirect('acadInfo')
    else:
        form = PerForm
    return render(request, 'per_info.html', {'form':form()})

def acadInfo(request):

    if request.method == 'POST':
        form = AcadForm(request.POST)
        if form.is_valid():
            AcademicInfo = form.save(commit = False)
            AcademicInfo.save()
            return redirect('addInfo')
    else:
        form = AcadForm
    return render(request, 'acad_info.html', {'form':form()})

def addInfo(request):

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            AdditionalInfo = form.save(commit = False)
            AdditionalInfo.save()
            return redirect('logInfo')
    else:
        form = AddForm
    return render(request, 'add_info.html', {'form':form()})

def logInfo(request):

    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            Login = form.save(commit = False)
            Login.save()
            return redirect('display')
    else:
        form = LogForm
    return render(request, 'login_info.html', {'form':form()})

def display(request):
    try:
      Student = Login.objects.all()
    except Login.DoesNotExist:
       raise Http404("Comment does not exist")
    return render(request, 'display.html',{'Student': Student})

def registerSuccess(request):
    try:
      login_details = Login.objects.all()
    except Login.DoesNotExist:
       raise Http404("Login does not exist") 
    return render(request, 'registerSuccess.html', {'login_details': login_details})
# Create your views here.
