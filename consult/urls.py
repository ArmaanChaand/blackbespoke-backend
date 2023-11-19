from django.urls import path
from .views import appointment_create, appointment_read, appointment_update
urlpatterns = [
   path('create/', appointment_create, name='appointment-create'),
   path('read/', appointment_read, name='appointment-read'),
   path('update/<str:pk>/', appointment_update, name='appointment-update')
]