from django.db import models
from clients.models import Client
from produits.models import Produit


class Commande(models.Model):
    STATUS = (('en attente', 'en attente'),
              ('refusée', 'refusée'),
              ('livré', 'livré'),)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    statu = models.CharField(max_length=100, null=False, choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True)
