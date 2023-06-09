# Generated by Django 3.2.19 on 2023-06-16 20:44

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('jobs', '0009_alter_vacancy_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
            managers=[
                ('jobseeker', django.db.models.manager.Manager()),
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JobseekerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('applications', models.ManyToManyField(blank=True, related_name='applicants', to='jobs.Vacancy')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favoriters', to='jobs.Vacancy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.jobseeker')),
            ],
        ),
    ]
