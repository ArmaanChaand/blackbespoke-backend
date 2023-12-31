from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    pass


class Customer(models.Model):
    is_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone     = PhoneNumberField(null=False, blank=False)
    email     = models.EmailField(null=False, blank=False)

    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs):
        self.full_name = self.full_name.title()
        super(Customer, self).save(*args, **kwargs)