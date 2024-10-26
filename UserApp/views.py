# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserRegistrationForm
from .models import RUser
from django.contrib.auth import authenticate, login as auth_login
def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "FARMER"
            user.set_password(form.cleaned_data["password"])
            user.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserRegistrationForm()
    return render(request, "register.html", {"form": form})



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            if user.role == "ADMIN":
                return redirect("dashboard_admin")
            else:
                return redirect("dashboard_farmer")
        else:
            print("User NFound")
            messages.error(request, "Invalid email or password.")
    
    return render(request, "login.html")

def dashboard_admin(request):
    
    return render(request, "dashboard_admin.html")


def dashboard_farmer(request):
    
    return render(request, "dashboard_farmer.html")
