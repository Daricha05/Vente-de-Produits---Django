from django.urls import path
from .views import Home, detail, panier, add_to_cart, update_cart_item, remove_from_cart

app_name = 'produits'

urlpatterns = [
    path('', Home, name='home'),
    path('detail/<int:id>/', detail, name='detail'),
    path('panier', panier, name='panier'),
    path('panier/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('panier/modifier/<int:item_id>/',
         update_cart_item, name='update_cart_item'),
    path('panier/supprimer/<int:item_id>/',
         remove_from_cart, name='remove_from_cart'),

]
