from django.shortcuts import render, redirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import *

# Create your views here.
@login_required
def index(request):
    return render(request, template_name='index.html')

@login_required
def assignments(request):
    return render(request, template_name='assignments.html')

@login_required
def statistics(request):
    return render(request, template_name='statistics.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

