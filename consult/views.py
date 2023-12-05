from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from user.models import Customer

@api_view(['POST'])
def appointment_create(request):
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def appointment_read(request):
    if request.method == 'GET':
        appointments = Appointment.objects.filter(is_active=True)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def address_read_one(request, customer_id):
    if request.method == 'GET':
        try:
            customer_instance = Customer.objects.get(id=customer_id)
            address =  Appointment.objects.filter(customer=customer_instance, is_active=True)
            if address is not None:
                serializer = AppointmentSerializer(address.first(), many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Zero addresses found'}, status=status.HTTP_404_NOT_FOUND)

        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def appointment_update(request, pk):
    try:
        address_detail = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AppointmentSerializer(address_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)