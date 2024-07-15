# Generated by Django 5.0.1 on 2024-07-15 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('en attente', 'En attente'), ('traitement', 'En cours de traitement'), ('livré', 'Livré'), ('annulée', 'Annulée')], default='en attente', max_length=100)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produits.produit')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommandeProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commandes.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produits.produit')),
            ],
        ),
    ]
