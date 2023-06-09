# Generated by Django 3.2.19 on 2023-06-21 20:37

import cloudinary_storage.storage
from django.db import migrations, models
import jobportal.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_resume_experience_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='cv',
            field=models.FileField(blank=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='cv/', validators=[jobportal.validators.FileValidator(content_types=('application/pdf', 'application/msword', 'text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), max_size=524288)]),
        ),
    ]
