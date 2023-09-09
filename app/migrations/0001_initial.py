# Generated by Django 4.2.1 on 2023-09-08 07:48

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Company', models.CharField(blank=True, max_length=100)),
                ('Api', models.IntegerField(choices=[(1, 'paymeny_gateway'), (2, 'social_media'), (3, 'weather_data_api')])),
                ('Feedback', models.IntegerField(choices=[(1, 'Bug_Type'), (2, 'Feature_request'), (3, 'General Feedback'), (4, 'Userability_issue'), (5, 'other')])),
                ('Feedback_detail', models.CharField(max_length=100)),
                ('severity', models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high'), (4, 'critical')])),
                ('reproducibility', models.IntegerField(choices=[(1, 'always'), (2, 'sometimes'), (3, 'rarely'), (4, 'unable_to_reproduce')])),
                ('step_to_reproduce', models.CharField(max_length=100)),
                ('attachment', models.FileField(blank=True, max_length=255, null=True, upload_to=app.models.Feedback.nameFile)),
                ('os', models.IntegerField(choices=[(1, 'window'), (2, 'macOs'), (3, 'android'), (4, 'ios'), (5, 'other')])),
                ('browser', models.CharField(max_length=100)),
                ('api_version', models.CharField(max_length=100)),
                ('overall_satisfication', models.IntegerField(choices=[(1, 'very_satisfied'), (2, 'satisfied'), (3, 'neutral'), (4, 'unsatisfied'), (5, 'very_unsatisfied')])),
                ('comment', models.CharField(max_length=100)),
                ('contacted', models.BooleanField()),
            ],
        ),
    ]
