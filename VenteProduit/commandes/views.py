from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Commande, CommandeProduit
# from clients.models import Client
from commandes.forms import CommandeForm
from produits.models import Panier


@login_required(login_url='login')
def Home(request):
    commandes = Commande.objects.all()[:10]
    # clients = Client.objects.all()

    context = {
        'commandes': commandes,
        # 'clients': clients,
    }

    return render(request, 'commandes/liste_commande.html', context)


@login_required(login_url='login')
def detail_commande(request, id):
    commande = get_object_or_404(Commande, id=id)
    return render(request, 'commandes/detail_commande', {'commande': commande})


@login_required(login_url='login')
def create_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commande')
    else:
        form = CommandeForm()

    return render(request, 'commandes/liste_commande.html', {'form': form})


@login_required(login_url='login')
def updateCommande(request, id):
    print("========== update")
    commande = get_object_or_404(Commande, id=id)  # Recupération ID commande
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)

        if form.is_valid():
            form.save()
            return redirect('commandes:Home')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'commandes/update-commande.html', {'form': form})


@login_required(login_url='login')
def deleteCommande(request, pk):
    commande = Commande.objects.get(pk=pk)
    commande.delete()
    return redirect('homeProduct')


@login_required(login_url='login')
def checkout(request):
    print("========== checkout")
    cart_items = Panier.objects.filter(user=request.user)
    if not cart_items:
        messages.error(request, "Votre panier est vide.")
        return redirect('produits:panier')

    # Créer une nouvelle commande
    commande = Commande.objects.create(user=request.user)
    for item in cart_items:
        CommandeProduit.objects.create(
            commande=commande,
            produit=item.produit,
            quantite=item.quantite
        )
        print(f"====={commande}, {item.produit}, {item.quantite}=====")
        # Optionnel : Réduire le stock du produit
        item.produit.stock -= item.quantite
        item.produit.save()

    # Vider le panier de l'utilisateur
    cart_items.delete()

    messages.success(request, "Votre commande a été passée avec succès.")
    return redirect('produits:home')
