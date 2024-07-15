from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produit, Panier


@login_required(login_url='login')
def Home(request):
    produits = Produit.objects.filter(disponible=True)

    context = {'produits': produits}

    return render(request, 'produits/index.html', context)


@login_required(login_url='login')
def detail(request, id):
    produit = get_object_or_404(Produit, id=id, disponible=True)
    category = produit.category

    # Récupération de 5 premier articles en relation
    produit_lier = Produit.objects.filter(category=category).exclude(id=id)[:5]

    context = {
        'produit': produit,
        'produit_lier': produit_lier,
    }
    return render(request, 'produits/detail.html', context)


@login_required(login_url='login')
def panier(request):
    cart_items = Panier.objects.filter(user=request.user)
    return render(request, 'produits/panier.html', {'cart_items': cart_items})


@login_required(login_url='login')
def add_to_cart(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    cart_item, created = Panier.objects.get_or_create(
        user=request.user, produit=produit)

    if not created:
        cart_item.quantite += 1
    cart_item.save()

    return redirect('produits:panier')


@login_required(login_url='login')
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(Panier, id=item_id, user=request.user)
    produit = cart_item.produit
    if request.method == 'POST':
        quantite = int(request.POST.get('quantite', 1))
        if quantite > produit.stock:
            messages.error(
                request, f"La quantité demandée dépasse le stock disponible ({produit.stock}).")
        else:
            cart_item.quantite = quantite
            cart_item.save()
            messages.success(request, "La quantité a été mise à jour.")
    return redirect('produits:panier')


@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Panier, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Le produit a été retiré du panier.")
    return redirect('produits:panier')
