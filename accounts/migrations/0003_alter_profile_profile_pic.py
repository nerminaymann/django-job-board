# Generated by Django 5.0 on 2024-01-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_profile_pic.jpeg', null=True, upload_to='profile_pics/'),
        ),
    ]
