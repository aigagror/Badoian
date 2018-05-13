from django.db import models

# Create your models here.

class Problem(models.Model):
    question = models.TextField()

    answer = models.CharField(max_length=256)