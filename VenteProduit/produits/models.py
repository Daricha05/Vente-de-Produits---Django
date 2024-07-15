from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    nom = models.CharField(max_length=200, null=True, unique=True)

    def __str__(self) -> str:
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    prix = models.IntegerField()
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)
    images = models.ImageField(upload_to='media', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nom


class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'produit')

    def __str__(self) -> str:
        return f"{self.user} - {self.produit.nom} - {self.quantite}"
