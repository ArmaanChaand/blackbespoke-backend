from django.db import models
from datetime import datetime, date
from django.utils import timezone
# Create your models here.
class Appointment(models.Model):
    class appnt_types(models.TextChoices):
        CHOICE_ONE = 'CALLBACK', 'CALLBACK'
        CHOICE_TWO = 'MEASUREMENT', 'MEASUREMENT'
        CHOICE_THREE = 'CONSULTATION', 'CONSULTATION'
        CHOICE_FOUR = 'DRAFT', 'DRAFT'
    appnt_type = models.CharField(
        max_length=20,
        choices=appnt_types.choices,
        default=appnt_types.CHOICE_ONE
    )
    is_active = models.BooleanField(default=True)
    date = models.DateField(null=False, blank=False, default=timezone.now)
    time = models.TimeField(null=False, blank=False, default=timezone.now)
    customer = models.ForeignKey(to='user.Customer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.appnt_type} • {self.customer} • {self.date}"
