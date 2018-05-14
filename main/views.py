from django.shortcuts import render, redirect, HttpResponseRedirect
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

@login_required
def create_rounds(request):
    if request.method == 'POST':
        round_name = request.POST.get('round_name')
        q_1 = request.POST.get('q_1')
        a_1 = request.POST.get('a_1')

        q_2 = request.POST.get('q_2')
        a_2 = request.POST.get('a_2')

        q_3 = request.POST.get('q_3')
        a_3 = request.POST.get('a_3')

        # Create the problems
        p_1 = Problem(question=q_1, correct_answer=a_1)
        p_2 = Problem(question=q_2, correct_answer=a_2)
        p_3 = Problem(question=q_3, correct_answer=a_3)

        p_1.save()
        p_2.save()
        p_3.save()

        # Create the round
        new_round = Round(name=round_name)
        new_round.save()
        new_round.problems.add(p_1)
        new_round.problems.add(p_2)
        new_round.problems.add(p_3)
        new_round.save()


        return redirect('rounds')

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
