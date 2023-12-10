from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('', include('home.urls')),
    path('consult/', include('consult.urls')),
    path('suit/', include('suit.urls')),
]