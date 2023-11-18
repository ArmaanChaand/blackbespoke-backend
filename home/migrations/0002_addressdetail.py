# Generated by Django 4.2.7 on 2023-11-18 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customer'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('landmark', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=50)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to='home.city')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address', to='user.customer')),
            ],
        ),
    ]