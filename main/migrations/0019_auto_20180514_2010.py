# Generated by Django 2.0.1 on 2018-05-15 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_submission_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='points',
            field=models.TextField(blank=True, null=True),
        ),
    ]