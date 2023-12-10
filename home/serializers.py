from rest_framework import serializers
from .models import City, AddressDetail, Pictures

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = City
        fields = ['id', 'icon', 'name', 'code', 'state']

class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AddressDetail
        fields = ['id', 'address', 'landmark', 'pin_code', 'city', 'customer']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"
