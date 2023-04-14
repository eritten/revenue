from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import IncomingForm, OutgoingForm

# Create your views here.

def log_in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if request.method == "POST":
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "User does not exist")
    return render(request, "registration/login.html")

def log_out(request):
    logout(request)
    return render(request, "registration/logout.html")


@login_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@login_required
def incoming(request):
    form = IncomingForm()
    if request.method=="POST":
        form = IncomingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "dashboard/incoming.html", {"form": form})
    return render(request, "dashboard/incoming.html", {"form": form})


@login_required
def outgoing(request):
    form = OutgoingForm()
    if request.method=="POST":
        form = OutgoingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "dashboard/outgoing.html", {"form": form})
    return render(request, "dashboard/outgoing.html", {"form": form})

