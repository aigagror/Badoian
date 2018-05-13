from django.shortcuts import render, redirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, template_name='index.html')

def assignments(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, template_name='assignments.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

