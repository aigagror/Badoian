from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Problem(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=256)

class Round(models.Model):
    name = models.CharField(max_length=128)
    problems = models.ManyToManyField(Problem, related_name='rounds')
    image = models.ImageField(null=True, blank=True)


class Assignment(models.Model):
    due_time = models.DateTimeField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')

    submitted = models.DateTimeField(null=True, blank=True)
    started = models.DateTimeField(default=timezone.now)
    answers = models.TextField(default="") # Each answer is in its own line
    submission_image = models.ImageField(null=True, blank=True)