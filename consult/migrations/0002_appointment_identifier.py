# Generated by Django 4.2.7 on 2023-11-19 19:12

import consult.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='identifier',
            field=models.CharField(default=consult.models.generate_short_uuid, editable=False, error_messages={'unique': 'Appointment with this identifier already exists.'}, max_length=100, unique=True),
        ),
    ]
