from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse

from shopping_cart.forms import AddToCartForm
from artworks.models import Artwork
from .models import CartItem


def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    cart = request.session.get('cart', {})

    cart_items = []
    grand_total = 0 
    for artwork_id, quantity in cart.items():
        artwork = get_object_or_404(Artwork, id=artwork_id)

        # Check if 'quantity' is a dictionary and extract the actual quantity value
        if isinstance(quantity, dict) and 'quantity' in quantity:
            quantity_value = quantity['quantity']
        else:
            quantity_value = quantity
        
        subtotal = artwork.price * quantity_value
        grand_total += subtotal  

        cart_items.append({
            'artwork': artwork,
            'quantity': quantity_value,
            'subtotal': subtotal,
        })

    context = {'cart_items': cart_items, 'grand_total': grand_total} 
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


def update_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        
        # Update the cart item quantity directly in the view function
        cart = request.session.get('cart', {})
        cart[item_id] = int(quantity)

        # Save the updated cart to the session
        request.session['cart'] = cart
        request.session.modified = True

        return redirect('shopping_cart')
    else:
        return redirect('shopping_cart')


def delete_cart_item(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        
        # Remove the cart item directly in the view function
        cart = request.session.get('cart', {})
        if item_id in cart:
            del cart[item_id]
        request.session['cart'] = cart
        
        return redirect('shopping_cart')
    else:
        return redirect('shopping_cart')


