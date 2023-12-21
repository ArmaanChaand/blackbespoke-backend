from django.urls import path
from .views import appointment_create, appointment_read, appointment_update, appointment_read_one
urlpatterns = [
   path('create/', appointment_create, name='appointment-create'),
   path('read/all/', appointment_read, name='appointment-read'),
   path('read/<str:customer_id>/', appointment_read_one, name='appointment-read-one'),
   path('update/<str:pk>/', appointment_update, name='appointment-update')
]