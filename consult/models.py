from collections.abc import Iterable
from django.db import models
from datetime import datetime, date, time
from django.utils import timezone
import uuid
# Create your models here.

def generate_short_uuid():
    return str(uuid.uuid4())[:6]

class Appointment(models.Model):
    class appnt_types(models.TextChoices):
        CHOICE_ONE = 'CALLBACK', 'CALLBACK'
        CHOICE_TWO = 'MEASUREMENT', 'MEASUREMENT'
        CHOICE_THREE = 'CONSULTATION', 'CONSULTATION'
        CHOICE_FOUR = 'DRAFT', 'DRAFT'
    appnt_type = models.CharField(
        max_length=20,
        choices=appnt_types.choices,
        default=appnt_types.CHOICE_FOUR
    )
    is_active = models.BooleanField(default=True)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    customer = models.ForeignKey(to='user.Customer', on_delete=models.SET_NULL, null=True, blank=True)
    customer_address = models.ForeignKey(to='home.AddressDetail', on_delete=models.SET_NULL, null=True, blank=True)
    identifier = models.CharField(max_length=100, null=False, blank=False, unique=True, editable=False, default=generate_short_uuid,
                            error_messages={
                                     "unique": "Appointment with this identifier already exists."
                                    })
    

    def __str__(self) -> str:
        return f"{self.appnt_type} • {self.customer} • {self.date}"