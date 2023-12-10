from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import City, AddressDetail, Pictures
from .serializers import CitySerializer, AddressDetailSerializer, PictureSerializer
from user.models import Customer

@api_view(['GET'])
def city_read(request):
    if request.method == 'GET':
        cities = City.objects.filter(is_active=True)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def city_read_one(request, city_id):
    if request.method == 'GET':
        city = City.objects.filter(is_active=True, id=city_id).first()
        if(city is not None):
            serializer = CitySerializer(city, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error" : "City not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def address_read(request):
    if request.method == 'GET':
        addresses = AddressDetail.objects.filter(is_active=True)
        serializer = AddressDetailSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def address_read_one(request, customer_id):
    if request.method == 'GET':
        try:
            customer_instance = Customer.objects.get(id=customer_id)
            address =  AddressDetail.objects.filter(customer=customer_instance, is_active=True)
            if address is not None:
                serializer = AddressDetailSerializer(address.first(), many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Zero addresses found'}, status=status.HTTP_404_NOT_FOUND)

        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def address_create(request):
    if request.method == 'POST':
        serializer = AddressDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def address_update(request, pk):
    try:
        address_detail = AddressDetail.objects.get(pk=pk)
    except AddressDetail.DoesNotExist:
        return Response({'error': 'AddressDetail not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AddressDetailSerializer(address_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["GET"])
def read_pic_one(request, pic_id):
    try:
        pic = Pictures.objects.get(id=pic_id)
        serializer = PictureSerializer(pic)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Picture not found"}, status=status.HTTP_404_NOT_FOUND)
