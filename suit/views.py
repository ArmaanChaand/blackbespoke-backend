from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Fabric, BlazerPattern, WaistcoatPattern, WaistcoatLapel , PantStyle, ShirtColor, SuitPartDetail, SuitBuild
from .serializers import (
    FabricSerializer, BlazerPatternSerializer,WaistcoatPatternSerializer,WaistcoatLapelSerializer,
    PantStyleSerializer, ShirtColorSerializer,
    SuitPartDetailSerializer, SuitBuildSerializer)

# READ ALL
def read_all_template(Model, ModelSerializer):
    # instances = Model.objects.filter(is_active=True)
    instances = Model.objects.all()
    serializer = ModelSerializer(instances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def read_fabric_all(request):
    return read_all_template(Model=Fabric, ModelSerializer=FabricSerializer)

@api_view(http_method_names=["GET"])
def read_blazer_pattern_all(request):
    return read_all_template(Model=BlazerPattern, ModelSerializer=BlazerPatternSerializer)

@api_view(http_method_names=["GET"])
def read_waistcoat_pattern_all(request):
    return read_all_template(Model=WaistcoatPattern, ModelSerializer=WaistcoatPatternSerializer)

@api_view(http_method_names=["GET"])
def read_waistcoat_pattern_all(request):
    return read_all_template(Model=WaistcoatPattern, ModelSerializer=WaistcoatPatternSerializer)
    
@api_view(http_method_names=["GET"])
def read_waistcoat_lapel_all(request):
    return read_all_template(Model=WaistcoatLapel, ModelSerializer=WaistcoatLapelSerializer)

@api_view(http_method_names=["GET"])
def read_pant_style_all(request):
    return read_all_template(Model=PantStyle, ModelSerializer=PantStyleSerializer)

@api_view(http_method_names=["GET"])
def read_shirt_color_all(request):
    return read_all_template(Model=ShirtColor, ModelSerializer=ShirtColorSerializer)
    
@api_view(http_method_names=["GET"])
def read_suit_part_detail_one(request, detail_id):
    try:
        suit_part_detail = SuitPartDetail.objects.get(id=detail_id)
        serializer = SuitPartDetailSerializer(suit_part_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Suit part detail not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=["GET"])
def read_suit_build_one(request, suit_id):
    try:
        suit_build = SuitBuild.objects.get(id=suit_id)
        serializer = SuitBuildSerializer(suit_build)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Suit not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=["GET"])
def read_suit_build_all(request):
    return read_all_template(Model=SuitBuild, ModelSerializer=SuitBuildSerializer)

@api_view(http_method_names=["POST"])
def create_suit_build(request):
    serializer = SuitBuildSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
def update_suit_build(request, suit_id):
    try:
        suit = SuitBuild.objects.get(id=suit_id)
        serializer = SuitBuildSerializer(data=request.data, instance=suit)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"error": "Suit not found"}, status=status.HTTP_404_NOT_FOUND)
