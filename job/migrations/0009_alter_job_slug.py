# Generated by Django 5.0 on 2024-01-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
