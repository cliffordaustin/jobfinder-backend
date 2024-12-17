# Generated by Django 5.1.3 on 2024-12-17 15:56

import core.utils
import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_companyprofile_num_of_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofileimages',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=core.utils.company_image_thumbnail),
        ),
    ]
