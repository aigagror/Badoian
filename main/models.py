from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

# Create your models here.
class Meet(models.Model):
    class Meta:
        abstract = True

    GBML = 'GBML'
    MML = 'MML'
    NEAML = 'NEAML'
    LEAGUES = (
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
    SEVEN = 'SEVEN'

    CONTEST_INDEX = (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR, 'Four'),
        (FIVE, 'Five'),
        (SIX, 'Six'),
    )

    YEARS = [i for i in reversed(range(1996, timezone.now().year + 1))]

    league = models.CharField(choices=LEAGUES, max_length=64)
    contest_index = models.CharField(choices=CONTEST_INDEX, max_length=16)
    start_year = models.IntegerField(default=2018)

class CompetedMeet(Meet):
    def __str__(self):
        return '{} {} Contest {}'.format(self.league, self.start_year, self.get_contest_index_display())

class IndividualScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    competed_meet = models.ForeignKey(CompetedMeet, on_delete=models.CASCADE)

    def bar_width(self):
        return self.score / 18 * 100

class Round(Meet):
    ROUND_INDEX = (
        (Meet.ONE, 'One'),
        (Meet.TWO, 'Two'),
        (Meet.THREE, 'Three'),
        (Meet.FOUR, 'Four'),
        (Meet.FIVE, 'Five'),
        (Meet.SIX, 'Six'),
        (Meet.SEVEN, 'Seven'),
    )

    round_index = models.CharField(choices=ROUND_INDEX, max_length=16)

    correct_answers = models.TextField()
    file = models.FileField(null=True, blank=True)

    @property
    def correct_answers_list(self):
        ret = []
        lines = self.correct_answers.splitlines()
        count = 0
        for line in lines:
            bare = line.strip()
            if bare != '':
                ret.append(line)

        return ret

    @property
    def number_of_problems(self):
        return len(self.correct_answers_list)

    def __str__(self):
        return '{} {}-{} Contest {} Round {}'.format(self.league, self.start_year, self.start_year+1, self.get_contest_index_display(), self.get_round_index_display())


class Assignment(models.Model):
    due_time = models.DateTimeField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)

    def __str__(self):
        return '{} | Due {}'.format(self.round, self.due_time.strftime('%m/%d'))


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')

    submitted = models.DateTimeField(null=True, blank=True)
    started = models.DateTimeField(default=timezone.now)
    answers = models.TextField(default="") # Each answer is in its own line

    points = models.TextField(null=True, blank=True) # Each point corresponds to each answer. This field is only used for manual grading

    feedback = models.TextField(null=True, blank=True) # Each feedback corresponds to each answer

    file = models.FileField(null=True, blank=True)

    def score(self):
        # TODO
        return random.randint(0,18)

    def bar_width(self):
        return self.score() / 18 * 100
