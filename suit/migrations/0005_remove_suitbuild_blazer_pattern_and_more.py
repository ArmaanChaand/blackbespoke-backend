# Generated by Django 4.2.7 on 2023-12-10 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suit', '0004_blazerpattern_description_fabric_detail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suitbuild',
            name='blazer_pattern',
        ),
        migrations.RemoveField(
            model_name='suitbuild',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='suitbuild',
            name='pant_style',
        ),
        migrations.RemoveField(
            model_name='suitbuild',
            name='shirt_color',
        ),
        migrations.RemoveField(
            model_name='suitbuild',
            name='waistcoat_lapel',
        ),
        migrations.RemoveField(
            model_name='suitbuild',
            name='waistcoat_pattern',
        ),
    ]
