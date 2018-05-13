# Generated by Django 2.0.1 on 2018-05-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='answer',
            new_name='solution',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='submission',
        ),
        migrations.AddField(
            model_name='submission',
            name='answers',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Assignment'),
            preserve_default=False,
        ),
    ]
