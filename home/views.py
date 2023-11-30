from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import City, AddressDetail
from .serializers import CitySerializer, AddressDetailSerializer
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
        customer_id = request.query_params.get('customer_id', None)
        if(customer_id):
            try:
                customer_instance = Customer.objects.get(id=customer_id)
                addresses =  addresses.filter(customer=customer_instance)
            except Customer.DoesNotExist:
                return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressDetailSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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