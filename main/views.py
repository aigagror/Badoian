from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import *
from .models import *
from django.utils import dateparse

# Create your views here.
@login_required
def index(request):
    context = {
        'head_coaches': User.objects.filter(groups__name='Head Coach'),
        'coaches': User.objects.filter(groups__name='Coach'),
        'members': User.objects.filter(groups=None),
    }
    return render(request, template_name='index.html', context=context)

@login_required
def assignments(request):
    user = request.user

    rounds = Round.objects.all()
    assignments = Assignment.objects.all()

    for assignment in assignments:
        submission = Submission.objects.filter(user=user, assignment=assignment).first()
        assignment.submission = submission

    context = {
        'assignments': assignments,
        'rounds': rounds,
    }

    return render(request, template_name='assignments.html', context=context)

@login_required
def create_assignment(request):
    due_date = request.POST.get('due_date')
    due_date = dateparse.parse_date(due_date)
    round_id = request.POST.get('round_id')

    round = Round.objects.get(id=round_id)

    new_assignment = Assignment(round=round, due_time=due_date)
    new_assignment.save()

    return redirect('assignments')

@login_required
def delete_assignment(request):
    assignment_id = request.POST.get('assignment_id')

    assignment = Assignment.objects.get(id=assignment_id)

    assignment.delete()

    return redirect('assignments')

@login_required
def create_submission(request):
    assignment_id = request.POST.get('assignment_id')

    assignment = Assignment.objects.get(id=assignment_id)

    user = request.user

    new_submission = Submission(assignment=assignment, user=user)
    new_submission.save()

    return redirect('submission', submission_id=new_submission.id)

@login_required
def delete_submission(request):
    submission_id = request.POST.get('submission_id')
    submission = Submission.objects.get(id=submission_id)

    submission.delete()

    return redirect('assignments')


@login_required
def submission(request, submission_id):
    my_submission = Submission.objects.get(id=submission_id)

    user = request.user

    if my_submission.user != user:
        return HttpResponse('This submission is not yours')

    context = {
        'submission': my_submission,
    }

    return render(request, 'submission.html', context=context)

@login_required
def scores(request):
    return render(request, template_name='scores.html')

@login_required
def rounds(request):
    rounds = Round.objects.all()
    context = {
        'rounds': rounds,
        'Round': Round,
    }
    return render(request, template_name='rounds.html', context=context)

@login_required
def round_file(request, round_id):
    round = Round.objects.get(id=round_id)

    return HttpResponse(round.file, content_type='application/pdf')

@login_required
def create_rounds(request):
    if request.method == 'POST':
        round_name = request.POST.get('round_name')

        file = request.FILES['round_file']

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
        new_round = Round(name=round_name, file=file)
        new_round.save()
        new_round.problems.add(p_1)
        new_round.problems.add(p_2)
        new_round.problems.add(p_3)
        new_round.save()


        return redirect('rounds')

@login_required
def delete_round(request):
    round_id = request.POST.get('round_id')
    round = Round.objects.get(id=round_id)
    round.delete()

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
