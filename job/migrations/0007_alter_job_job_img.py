# Generated by Django 5.0 on 2023-12-30 14:54

import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_job_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_img',
            field=models.ImageField(upload_to=job.models.Uploaded_Images),
        ),
    ]
