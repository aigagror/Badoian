from django.shortcuts import render, redirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import *
from .models import *

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

@login_required
def rounds(request):
    return render(request, template_name='rounds.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST.get('team_name')

        new_team = Team(name=name)

        new_team.head_coaches = request.user

        new_team.save()

        return redirect('index')

@login_required
def join_team(request):
    if request.method == 'POST':
        team_id = int(request.POST.get('team_id'))

        team = Team.objects.get(id=team_id)

        team.members.add(request.user)

        team.save()
