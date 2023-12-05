from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Appointment
        fields = ['id', 'appnt_type', 'date', 'time', 'customer', 'suit', 'identifier', 'customer_address', 'customer_city']
    

