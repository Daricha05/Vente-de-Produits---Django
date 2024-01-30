from django.urls import path
from .views import Home, updateCommande, deleteCommande

urlpatterns = [
    path('', Home, name='homeCommand'),
    path('<int:pk>/', updateCommande, name='updateCom'),
    path('del/<int:pk>/', deleteCommande, name='deleteCom'),
]
