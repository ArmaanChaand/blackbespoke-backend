# Generated by Django 4.2.7 on 2023-11-30 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_addressdetail_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(default='state', max_length=50),
            preserve_default=False,
        ),
    ]