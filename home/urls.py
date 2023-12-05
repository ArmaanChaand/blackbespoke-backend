from django.urls import path
from .views import city_read, address_read, address_read_one, address_create, address_update, city_read_one

urlpatterns = [
    path('city/read/all/', city_read, name='city-read-all'),
    path('city/read/<str:city_id>/', city_read_one, name='city-read-one'),
    path('address/read/all/', address_read, name='address-read-all'),
    path('address/read/<str:customer_id>/', address_read_one, name='address-read-one'),
    path('address/create/', address_create, name='address-create'),
    path('address/update/<str:pk>/', address_update, name='address-update')
]