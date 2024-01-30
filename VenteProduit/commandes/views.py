from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Commande
from clients.models import Client
from commandes.forms import CommandeForm


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
