from django.contrib import admin
from .models import Produit, Category


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'date_creation')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom',)
