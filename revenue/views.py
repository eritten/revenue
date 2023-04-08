from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    pass

def log_in(request):
    pass

def log_out(request):
    pass

@login_required
def dashboard(request):
    pass
