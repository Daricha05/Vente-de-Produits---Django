from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=User.objects.get(username='django'))
    phone = models.CharField(max_length=15)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Client: {self.user.username}"
