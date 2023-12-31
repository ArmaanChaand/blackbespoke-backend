from rest_framework import serializers
from .models import Customer
from utils.validators import validate_letters_and_spaces

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = ['id', 'full_name', 'email', 'phone']
    
    def validate_full_name(self, value):
        if not validate_letters_and_spaces(value):
            raise serializers.ValidationError("Only letters and spaces are allowed.")
        return value

