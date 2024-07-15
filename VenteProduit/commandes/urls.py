from django.urls import path
from .views import Home, detail_commande, deleteCommande, create_commande, checkout


urlpatterns = [
    path('', Home, name='commande'),
    path('<int:id>/', detail_commande, name='detail_commande'),
    path('create/', create_commande, name='create_commande'),
    path('del/<int:pk>/', deleteCommande, name='deleteCom'),
    path('checkout/', checkout, name='checkout'),
]
