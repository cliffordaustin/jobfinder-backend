# Generated by Django 5.1.3 on 2024-12-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_seeker_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary_type',
            field=models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=255, null=True),
        ),
    ]
