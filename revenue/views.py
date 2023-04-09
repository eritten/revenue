from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
    form = SignUpForm(request.POST)
        if form.is_valid():
        form.save()
        messages.success(request, "Your account have been created")
    return render(request, "signup.html", {"form": form})

def log_in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if request.method == "POST":

        if not user:
            messages.error(request, "User does not exist")
        login(request, user)

        return redirect("dashboard")

    return render(request, "registration/signup.html")

def log_out(request):
    logout(request, user)
    return render(request, "logout.html")


@login_required
def dashboard(request):
    return render(request, "home/dashboard.html")
