# Generated by Django 2.0.1 on 2018-05-17 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_round_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='name',
        ),
    ]
