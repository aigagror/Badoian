from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Problem(models.Model):
    question = models.TextField()

    answer = models.CharField(max_length=256)

class Round(models.Model):
    problems = models.ManyToManyField(Problem, related_name='Round')

    image = models.ImageField()


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    submission = models.CharField(max_length=256)