# Generated by Django 3.2.19 on 2023-07-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer', '0006_alter_employerprofile_company'),
        ('jobs', '0016_auto_20230710_1823'),
        ('jobseeker', '0009_alter_jobseekerprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_notifications', to='jobs.application')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_notifications', to='employer.employer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_notifications', to='jobseeker.jobseekerprofile')),
            ],
            options={
                'verbose_name_plural': 'application_notifications',
                'ordering': ['-timestamp'],
            },
        ),
    ]