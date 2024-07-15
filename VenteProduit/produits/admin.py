from django.contrib import admin
from .models import Produit, Category, Panier


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix',
                    'date_creation', 'stock', 'disponible')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom',)


@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('user', 'produit', 'quantite', 'date_ajout')
