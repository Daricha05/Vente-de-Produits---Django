from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Client
from .forms import ClientForm
from commandes.filters import CommandFilter


@login_required(login_url='login')
def Home(request, pk):
    client = Client.objects.get(pk=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()

# Filtrage de commande

    # Liaison filte avec la commande
    myFilter = CommandFilter(request.GET, queryset=commande)
    commande = myFilter.qs  # Mise en jour de l'affichage du tableau

    context = {
        'client': client,
        'commande_total': commande_total,
        'commande': commande,
        'myFilter': myFilter,
    }
    return render(request, 'clients/index.html', context)


@login_required(login_url='login')
def ListClient(request):
    clients = Client.objects.all()
    return render(request, 'clients/list.html', {'clients': clients})


@login_required(login_url='login')
def addClient(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        phone = request.POST.get('phone')

        client = Client.objects.create(nom=nom, prenom=prenom, phone=phone)
        client.save()
        return redirect('listClient')

    else:
        return render(request, 'clients/add.html')


@login_required(login_url='login')
def upClient(request, pk):
    client = Client.objects.get(pk=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return redirect('listClient')

    return render(request, 'clients/updateClient.html', {'form': form})


def delClient(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    return redirect('listClient')



