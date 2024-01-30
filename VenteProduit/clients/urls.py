from django.urls import path
from .views import Home, ListClient, addClient, delClient, upClient


urlpatterns = [
    path('<int:pk>/', Home, name='homeClient'),
    path('Listes/', ListClient, name='listClient'),
    path('Add/', addClient, name='newClient'),
    path('Del/<int:pk>', delClient, name='delClient'),
    path('Edit/<int:pk>', upClient, name='upClient'),
]
