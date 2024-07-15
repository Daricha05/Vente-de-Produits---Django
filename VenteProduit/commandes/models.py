from django.contrib.auth.models import User
from django.db import models
from produits.models import Produit


class Commande(models.Model):
    STATUS_CHOICES = (
        ('en attente', 'En attente'),
        ('traitement', 'En cours de traitement'),
        ('livré', 'Livré'),
        ('annulée', 'Annulée'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="en attente")
    date_creation = models.DateTimeField(auto_now_add=True)
    # produits = models.ManyToManyField(Produit, through='CommandeProduit')

    def __str__(self):
        return f"Commande {self.id} pour {self.user.username}"


class CommandeProduit(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite} (Commande {self.commande.id})"
