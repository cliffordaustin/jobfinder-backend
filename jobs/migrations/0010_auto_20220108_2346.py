# Generated by Django 3.2.9 on 2022-01-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_job_number_of_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='remote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
