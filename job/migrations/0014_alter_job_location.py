# Generated by Django 5.0 on 2024-02-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_job_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]