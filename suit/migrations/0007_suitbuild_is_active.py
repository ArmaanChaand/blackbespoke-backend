# Generated by Django 4.2.7 on 2023-12-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suit', '0006_suitbuild_blazer_pattern_suitbuild_fabric_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitbuild',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]