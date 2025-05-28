from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request,"hr/home.html")

def sample(request):
    return render(request , "home.html")