# Generated by Django 5.0.1 on 2024-07-15 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='produits',
        ),
    ]
