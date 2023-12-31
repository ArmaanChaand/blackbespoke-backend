from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer
from consult.models import Appointment
from .serializers import CustomerSerializer


@api_view(['GET'])
def customer_read_one(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

        
@api_view(['GET'])
def customer_read(request):
    if request.method == 'GET':
        customers = Customer.objects.filter(is_active=True)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def customer_create(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def customer_update(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
        if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data, instance=customer)
            if serializer.is_valid():
                serializer.save()
                try:
                    appointment = customer.my_consult
                    # Pass
                except:
                    Appointment.objects.create(customer=customer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
