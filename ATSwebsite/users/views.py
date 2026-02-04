from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("formis valid")
            form.save()
            return redirect("login")
    else :
        form = RegisterForm()
        return render(request, "users/register.html", {"form" : form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(request, username=username, password=password)
        print("AUTH USER:", user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")   # change to your page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "users/login.html")

#logout

def logout_view(request):
    logout(request)
    return redirect("login")

        
