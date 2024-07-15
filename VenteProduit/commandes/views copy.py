from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Commande
from clients.models import Client
from commandes.forms import CommandeForm
from produits.models import Panier


@login_required(login_url='login')
def Home(request):
    commandes = Commande.objects.all()[:10]
    clients = Client.objects.all()

    # ajouter une nouvelle commande
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homeCommand')

    context = {
        'commandes': commandes,
        'clients': clients,
        'form': form,
    }

    return render(request, 'commandes/liste_commande.html', context)


@login_required(login_url='login')
def updateCommande(request, pk):
    commande = Commande.objects.get(pk=pk)  # Recupération ID commande
    form = CommandeForm(instance=commande)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)

        if form.is_valid():
            form.save()
            return redirect('homeCommand')

    return render(request, 'commandes/update-commande.html', {'form': form})


@login_required(login_url='login')
def deleteCommande(request, pk):
    commande = Commande.objects.get(pk=pk)
    commande.delete()
    return redirect('homeProduct')


@login_required(login_url='login')
def create_order(request):
    cart_items = Panier.objects.filter(user=request.user)

    if cart_items:
        commande = Commande.objects.create(user=request.user)

        for item in cart_items:
            commande.items.create(produit=item.produit, quantite=item.quantite)
            item.delete()
        return redirect('commandes:detail_commande')
    return redirect('produits:panier')


@login_required(login_url='login')
def detail_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    return render(request, 'commandes/detail_commande', {'commande': commande})
