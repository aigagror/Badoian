# Generated by Django 2.0.1 on 2018-05-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20180517_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='submission_file',
            new_name='file',
        ),
    ]
