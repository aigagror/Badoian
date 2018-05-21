from main.models import *
from django.core.files import File

all_rounds = Round.objects.all()
all_rounds.delete()

months = [10,11,12,1,2,3]
for year in range(2003,2017):
    for month in months:
        mont_str = "{0:0=2d}".format(month)

        for round_index in range(6):
            file = open('mml_files/mml/{}_{}/{}.pdf'.format(year if month > 3 else year + 1, mont_str, round_index), 'rb')

            correct_answers = 'unknown\nunknown\nunknown'
            new_round = Round(start_year=year, contest_index=Meet.CONTEST_INDEX[months.index(month)][0],
                              round_index=Round.ROUND_INDEX[round_index][0], file=File(file), league='MML',
                              correct_answers=correct_answers)
            new_round.save()

