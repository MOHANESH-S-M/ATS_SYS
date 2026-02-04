from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import jobpost
from .forms import jobpostForm
# Create your views here.


@login_required(login_url='login')
def home(request):
    jobs = jobpost.objects.filter(hr=request.user)
    return render(request,"hr/home.html",{"jobs":jobs})


# This is for job creation
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

@login_required(login_url='login')
def editjob(request,slug):
    job = get_object_or_404(jobpost, slug=slug, hr=request.user)

    if request.method == 'POST':
        form = jobpostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = jobpostForm(instance=job)

    return render(request, "hr/editjob.html", {"form": form})


@login_required(login_url='login')
def deletejob(request,slug):
    job = get_object_or_404(jobpost,slug=slug,hr=request.user)
    if request.method == "POST":
        job.delete()
        return redirect('home')
    return render(request,'hr/deletejob.html',{"job":job})




    
