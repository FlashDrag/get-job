# Generated by Django 3.2.19 on 2023-06-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0006_auto_20230625_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='address',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
