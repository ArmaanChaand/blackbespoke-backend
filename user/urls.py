from django.urls import path
from .views import customer_read, customer_read_one, customer_create, customer_update
urlpatterns = [
    path('customer/read/all/', customer_read, name='customer-read-all'),
    path('customer/read/<str:customer_id>/', customer_read_one, name='customer-read-one'),
    path('customer/create/', customer_create, name='customer-create-one'),
    path('customer/update/<str:customer_id>/', customer_update, name='customer-update-one'),
]