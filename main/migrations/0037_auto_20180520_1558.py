# Generated by Django 2.0.1 on 2018-05-20 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20180518_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='points',
            new_name='correct',
        ),
    ]
