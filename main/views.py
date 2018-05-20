from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import *
from .models import *
from django.utils import dateparse
from django.contrib.auth.models import Group

# Create your views here.
@login_required
def promote(request):
    user_id = request.POST.get('user_id')

    head_coach_group = Group.objects.get(name='Head Coach')
    coach_group = Group.objects.get(name='Coach')
    member_group = Group.objects.get(name='Player')

    user = User.objects.get(id=user_id)

    if head_coach_group in user.groups.all():
        foo = 0
    elif coach_group in user.groups.all():
        user.groups.clear()
        user.groups.add(head_coach_group)

    elif member_group in user.groups.all():
        user.groups.clear()
        user.groups.add(coach_group)

    else:
        user.groups.clear()
        user.groups.add(member_group)

    return redirect('index')

@login_required
def demote(request):
    user_id = request.POST.get('user_id')

    head_coach_group = Group.objects.get(name='Head Coach')
    coach_group = Group.objects.get(name='Coach')
    member_group = Group.objects.get(name='Player')

    user = User.objects.get(id=user_id)

    if head_coach_group in user.groups.all():
        user.groups.clear()
        user.groups.add(coach_group)

    elif coach_group in user.groups.all():
        user.groups.clear()
        user.groups.add(member_group)

    elif member_group in user.groups.all():
        user.groups.clear()


    return redirect('index')


@login_required
def player(request, user_id):
    user = User.objects.get(id = user_id)
    assignments = Assignment.objects.all()
    for assignment in assignments:
        submission = Submission.objects.filter(user=user, assignment=assignment).first()
        assignment.submission = submission

    competed_meets = CompetedMeet.objects.all()
    for meet in competed_meets:
        individual_score = IndividualScore.objects.filter(user=user, competed_meet=meet).first()
        meet.score = individual_score.score if individual_score is not None else None
        meet.bar_width = meet.score / 18 * 100 if meet.score is not None else None

    context = {
        'user': user,
        'competed_meets': competed_meets,
        'assignments': assignments
    }
    return render(request, 'player.html', context)

@login_required
def index(request):

    def add_scores(users):
        for user in users:
            # TODO
            user.score = 0
            user.bar_width = 0
        return users

    context = {
        'head_coaches': add_scores(User.objects.filter(groups__name='Head Coach')),
        'coaches': add_scores(User.objects.filter(groups__name='Coach')),
        'players': add_scores(User.objects.filter(groups__name='Player')),
        'non_players': add_scores(User.objects.filter(groups=None)),
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
def assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)

    context = {
        'assignment': assignment,
    }

    return render(request, 'assignment.html', context)

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
def submit_submission(request):
    submission_id = request.POST.get('submission_id')

    submission = Submission.objects.get(id=submission_id)

    answers = [request.POST.get('answer_{}'.format(i)) for i in range(1, submission.assignment.round.number_of_problems + 1)]

    submission.answers = '\n'.join(answers)

    if len(request.FILES) > 0:
        # Submit file for manual grading
        file = request.FILES[0]
        submission.file = file

    submission.submitted = timezone.now()
    submission.save()

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
def create_competed_meet(request):
    league = request.POST.get('league')
    start_year = request.POST.get('start_year')
    contest_index = request.POST.get('contest_index')

    competed_meet = CompetedMeet(league=league, start_year=start_year, contest_index=contest_index)
    competed_meet.save()

    return redirect('scores')

@login_required
def delete_competed_meet(request):
    meet_id = request.POST.get('competed_meet_id')
    competed_meet = CompetedMeet.objects.get(id=meet_id)
    competed_meet.delete()

    return redirect('scores')

@login_required
def scores(request):
    assignments = Assignment.objects.all()
    for assignment in assignments:
        members = User.objects.all()
        for member in members:
            try:
                member_submission = Submission.objects.get(user=member, assignment=assignment)
            except:
                member_submission = None

            member.score = member_submission.score() if member_submission is not None else 0
            member.bar_width = member.score / 18 * 100

        assignment.members = members

    competed_meets = CompetedMeet.objects.all()
    for meet in competed_meets:
        players = User.objects.exclude(groups=None).exclude(groups__name='Head Coach')
        for player in players:
            individual_score = IndividualScore.objects.filter(competed_meet=meet, user=player).first()
            player.score = individual_score.score if individual_score is not None else None
            player.bar_width = player.score / 18 * 100 if player.score is not None else None

        meet.players = players

    context = {
        'assignments': assignments,
        'competed_meets': competed_meets,
        'Meet': Meet
    }
    return render(request, template_name='scores.html', context=context)

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
        league = request.POST.get('league')
        contest_index = request.POST.get('contest_index')
        start_year = request.POST.get('start_year')

        round_index = request.POST.get('round_index')

        file = request.FILES['round_file']

        a_1 = request.POST.get('a_1')

        a_2 = request.POST.get('a_2')

        a_3 = request.POST.get('a_3')

        # Create the problems
        correct_answers = '\n'.join([a_1, a_2, a_3])

        # Create the round
        new_round = Round(file=file, correct_answers=correct_answers,
                          round_index=round_index, league=league,
                          contest_index=contest_index, start_year=start_year)
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

