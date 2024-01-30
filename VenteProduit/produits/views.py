from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produit


@login_required(login_url='login')
def Home(request):
    produits = Produit.objects.all()

    context = {'produits': produits}

    return render(request, 'produits/index.html', context)


@login_required(login_url='login')
def detail(request, id):
    produit = Produit.objects.get(id=id)
    category = produit.category

    # Récupération de 5 premier articles en relation avec autre
    produit_lier = Produit.objects.filter(category=category)[:5]

    context = {
        'produit': produit,
        'produit_lier': produit_lier,
    }
    return render(request, 'produits/detail.html', context)
