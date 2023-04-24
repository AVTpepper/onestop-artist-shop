from django.shortcuts import render, redirect, get_object_or_404
from shopping_cart.forms import AddToCartForm
from artworks.models import Artwork
from .models import CartItem


def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    cart = request.session.get('cart', {})

    cart_items = []
    for artwork_id, quantity in cart.items():
        artwork = get_object_or_404(Artwork, id=artwork_id)

        # Check if 'quantity' is a dictionary and extract the actual quantity value
        if isinstance(quantity, dict) and 'quantity' in quantity:
            quantity_value = quantity['quantity']
        else:
            quantity_value = quantity
        
        cart_items.append({
            'artwork': artwork,
            'quantity': quantity_value,
            'subtotal': artwork.price * quantity_value,
        })

    context = {'cart_items': cart_items}
    return render(request, 'shopping_cart/cart.html', context)


def add_to_cart(request, artwork_id):
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            artwork_id = form.cleaned_data['artwork_id']
            quantity = form.cleaned_data['quantity']
            artwork = get_object_or_404(Artwork, id=artwork_id)

            cart = request.session.get('cart', {})

            if artwork_id in cart:
                cart[artwork_id]['quantity'] += quantity
            else:
                cart[artwork_id] = {'quantity': quantity}

            request.session['cart'] = cart

            return redirect('shopping_cart')

    return redirect('home')
