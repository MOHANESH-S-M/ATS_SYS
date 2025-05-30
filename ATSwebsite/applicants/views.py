from django.shortcuts import render,redirect,get_object_or_404
from .forms import ApplicationForm
from hr.models import jobpost
from django.contrib import messages


# Create your views here.
# this is for job apply
def apply_to_job(request,slug):
    job = get_object_or_404(jobpost,slug=slug)
    if not job.is_expired():
        return render(request,'applicants/job_expired.html',{"job":job})
    if request.method == "POST":
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request,"Application Submitted Successfully")
            return redirect('apply-success')
    else:
        form = ApplicationForm()
    return render(request,"applicants/apply_form.html",{"form":form ,"job":job})


# This is only to produce success
def apply_success(request):
    return render(request ,'applicants/apply_success.html')