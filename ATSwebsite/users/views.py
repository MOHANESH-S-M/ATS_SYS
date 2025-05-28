from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate , login ,logout
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


# login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username ,password = password)
        if user:
            login(request,user)
            return redirect("home")
    return render(request ,"users/login.html")

#logout

def logout_view(request):
    logout(request)
    return redirect("login")

        
