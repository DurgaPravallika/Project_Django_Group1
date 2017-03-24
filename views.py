from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import AdditionalInfoForm
from .models import AdditionalInfo


def index(request):
    if request.method == "POST":
        form = AdditionalInfoForm(request.POST) 
        if form.is_valid():		
            AdditionalInfo = form.save(commit = False)
            AdditionalInfo.save()            
            return redirect('success')
        
    else:
        form = AdditionalInfoForm()
    return render(request, "index.html", {'form': form})


def success(request):
			try:
				drive_details = AdditionalInfo.objects.all()
			except AdditionalInfo.DoesNotExist:
				raise Http404("DriveDetails does not exist")
			return render(request, 'viewDrives.html', {'drive_details': drive_details})
			
def display(request):
			try:
				Student = Drive.objects.all()
			except AdditionalInfo.DoesNotExist:
				raise Http404("Comment does not exist")
			return render(request, "display.html",{'Student': Student})
