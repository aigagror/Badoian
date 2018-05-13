# Generated by Django 2.0.1 on 2018-05-13 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20180513_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='coaches',
            field=models.ManyToManyField(related_name='coach_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='head_coaches',
            field=models.ManyToManyField(related_name='head_coach_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='round',
            name='problems',
            field=models.ManyToManyField(related_name='rounds', to='main.Problem'),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
    ]
