from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    pass


class Customer(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone     = PhoneNumberField(null=False, blank=False)
    email     = models.EmailField(null=False, blank=False)