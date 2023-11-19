from rest_framework import serializers
from .models import City, AddressDetail

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = City
        fields = ['id', 'icon', 'name', 'code']

class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AddressDetail
        fields = ['id', 'address', 'landmark', 'pin_code', 'city', 'customer']
