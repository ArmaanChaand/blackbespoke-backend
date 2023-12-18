from rest_framework import serializers
from .models import Fabric, BlazerPattern, WaistcoatPattern, WaistcoatLapel, PantStyle, ShirtColor, SuitPartDetail, SuitBuild

class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ["id", "name", "icon", "pictures", "detail"]

class BlazerPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlazerPattern
        fields = ["id", "name", "icon", "pictures", "description", "detail"]
        
class WaistcoatPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaistcoatPattern
        fields = ["id", "name", "icon", "pictures", "description", "detail"]
        
class WaistcoatLapelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaistcoatLapel
        fields = ["id", "name", "icon", "pictures", "description", "detail"]

class PantStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantStyle
        fields = ["id", "name", "icon", "pictures", "description", "detail"]

class ShirtColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtColor
        fields = ["id", "name", "color", "pictures", "detail"]

class SuitPartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SuitPartDetail
        fields = ["id","currency","price","composition","season","fineness","weight","description"]

class SuitBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SuitBuild
        fields = ["id","monogram_text","fabric","blazer_pattern","waistcoat_pattern","waistcoat_lapel","pant_style","shirt_color"]