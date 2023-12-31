from rest_framework import serializers
from .models import City, AddressDetail, Pictures, Testimonials

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = City
        fields = ['id', 'icon', 'name', 'code', 'state']

class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AddressDetail
        fields = ['id', 'address', 'landmark', 'pin_code', 'city', 'customer']
    
    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError('Address is required.')
        return value
        
    def validate_landmark(self, value):
        if not value:
            raise serializers.ValidationError('Landmark is required.')
        return value
        
    def validate_pin_code(self, value):
        if not value:
            raise serializers.ValidationError('Pincode is required.')
        return value

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = "__all__"

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"
