# Generated by Django 3.2.9 on 2021-11-14 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('num_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('year_started', models.PositiveIntegerField(blank=True, null=True)),
                ('about_company', models.TextField(blank=True, null=True)),
                ('values', models.TextField(blank=True, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfileImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('comment', models.TextField(blank=True, null=True)),
                ('company_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_images', to='company.companyprofile')),
            ],
        ),
    ]
