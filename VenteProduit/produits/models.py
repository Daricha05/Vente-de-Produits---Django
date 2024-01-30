from django.db import models


class Category(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.IntegerField()
    images = models.ImageField(upload_to='media', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.nom
