from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Problem(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=256)

class Round(models.Model):
    GBML = 'GBML'
    MML = 'MML'
    NEAML = 'NEAML'
    LEAGUE = (
        (GBML, 'Greater Boston Mathematics League'),
        (MML, 'Massachusetts Mathematics League'),
        (NEAML, 'New England Association of Math Leagues'),
    )

    ONE = 'ONE'
    TWO = 'TWO'
    THREE = 'THREE'
    FOUR = 'FOUR'
    FIVE = 'FIVE'
    SIX = 'SIX'
    ROUND_INDEX = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
    )

    CONTEST_INDEX = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
    )

    YEARS = [i for i in range(1996, timezone.now().year + 1)]

    league = models.CharField(choices=LEAGUE, max_length=64)
    round_index = models.CharField(choices=ROUND_INDEX, max_length=16)
    contest_index = models.CharField(choices=CONTEST_INDEX, max_length=16)

    year = models.IntegerField(default=2018)

    problems = models.ManyToManyField(Problem, related_name='rounds')
    file = models.FileField(null=True, blank=True)


class Assignment(models.Model):
    due_time = models.DateTimeField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')

    submitted = models.DateTimeField(null=True, blank=True)
    started = models.DateTimeField(default=timezone.now)
    answers = models.TextField(default="") # Each answer is in its own line
    points = models.TextField(null=True, blank=True) # Each point corresponds to each answer
    feedback = models.TextField(null=True, blank=True) # Each feedback corresponds to each answer
    submission_image = models.ImageField(null=True, blank=True)