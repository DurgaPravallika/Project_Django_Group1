from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import AcademicInfoForm
from .models import AcademicInfo


def index(request):
    if request.method == "POST":
        form = AcademicInfoForm(request.POST) 
        if form.is_valid():		
            AcademicInfo = form.save(commit = True)
            AcademicInfo.save()            
            return redirect('success')
        
    else:
        form = AcademicInfoForm()
    return render(request, "index.html", {'form': form})


def success(request):
			try:
				drive_details = AcademicInfo.objects.all()
			except AcademicInfo.DoesNotExist:
				raise Http404("DriveDetails does not exist")
			return render(request, 'success.html', {'drive_details': drive_details})
			
def display(request):
			try:
				Student = AcademicInfo.objects.all()
			except AcademicInfo.DoesNotExist:
				raise Http404("Comment does not exist")
			return render(request, "display.html",{'Student': Student})

