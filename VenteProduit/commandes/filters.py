import django_filters
from .models import Commande


class CommandFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ['produit', 'status']
