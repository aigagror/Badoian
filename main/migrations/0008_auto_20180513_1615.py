# Generated by Django 2.0.1 on 2018-05-13 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180513_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='time',
            new_name='submitted',
        ),
    ]