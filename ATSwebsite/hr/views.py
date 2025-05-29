from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import jobpost
from .forms import jobpostForm
# Create your views here.


@login_required(login_url='login')
def home(request):
    jobs = jobpost.objects.filter(hr=request.user)
    return render(request,"hr/home.html",{"jobs":jobs})

@login_required(login_url='login')
def createjob(request):
    if request.method == 'POST':
        form = jobpostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.hr = request.user
            job.save()
            return redirect('home')
    else:
        form = jobpostForm()
    return render(request,"hr/create-job.html",{"form":form})

