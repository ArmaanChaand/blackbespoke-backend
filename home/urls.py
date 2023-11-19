from django.urls import path
from .views import city_read, address_read, address_create, address_update

urlpatterns = [
    path('city/read/all/', city_read, name='city-read-all'),
    path('address/read/all/', address_read, name='address-read-all'),
    path('address/create/', address_create, name='address-create'),
    path('address/update/<str:pk>/', address_update, name='address-update')
]