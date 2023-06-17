# Generated by Django 3.2.19 on 2023-06-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_auto_20230617_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='resume',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='status',
            field=models.CharField(choices=[('IN_REVIEW', 'In Review'), ('ACTIVE', 'Active'), ('WITHDRAWN', 'Withdrawn'), ('CLOSED', 'Closed')], default='IN_REVIEW', max_length=50),
        ),
    ]
