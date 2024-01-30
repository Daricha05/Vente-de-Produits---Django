from django.db import models


class Client(models.Model):
    nom = models.CharField(max_length=150, null=True)
    prenom = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"
