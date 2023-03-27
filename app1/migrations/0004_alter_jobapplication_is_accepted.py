# Generated by Django 4.1.7 on 2023-03-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_candidate_job_is_active_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='is_accepted',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], max_length=50),
        ),
    ]
