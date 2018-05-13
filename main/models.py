from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Problem(models.Model):
    question = models.TextField()

    answer = models.CharField(max_length=256)

class Round(models.Model):
    problems = models.ManyToManyField(Problem, related_name='rounds')

    image = models.ImageField(null=True, blank=True)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    time = models.DateTimeField(default=timezone.now)

    submission = models.CharField(max_length=256)

    submission_image = models.ImageField(null=True, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=32)

    members = models.ManyToManyField(User, related_name='teams')

    coaches = models.ManyToManyField(User, related_name='coach_teams')

    head_coaches = models.ManyToManyField(User, related_name='head_coach_teams')