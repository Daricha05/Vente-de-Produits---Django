from django.contrib import admin
from .models import Commande, CommandeProduit


class CommandeProduitInline(admin.TabularInline):
    model = CommandeProduit
    extra = 1


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date_creation')
    inlines = [CommandeProduitInline]
