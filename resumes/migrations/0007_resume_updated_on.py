# Generated by Django 3.2.19 on 2023-06-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0006_alter_resume_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
