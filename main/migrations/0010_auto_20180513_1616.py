# Generated by Django 2.0.1 on 2018-05-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180513_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
