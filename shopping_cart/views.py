from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from artworks.models import Artwork

def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """
    return render(request, 'shopping_cart/cart.html')

def add_to_cart(request, artwork_id):
    """ Add a quantity of the specified artwork to the shopping cart """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    redirect_url = request.POST.get('redirect_url')
    
    # Check if quantity is specified in the POST request
    quantity = request.POST.get('quantity')
    if quantity is None:
        # If quantity is not specified, set default quantity to 1
        quantity = 1
    else:
        # Otherwise, convert quantity to an integer
        quantity = int(quantity)

    cart = request.session.get('shopping_cart', {})

    # Convert artwork_id to a string before comparing or storing it
    artwork_id_str = str(artwork_id)

    if artwork_id_str in list(cart.keys()):
        messages.info(request, f'{artwork.name} is already in your cart')
    else:
        cart[artwork_id_str] = quantity
        messages.success(request, f'Added {artwork.name} to your cart')

    request.session['shopping_cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, artwork_id):
    """Adjust the quantity of the specified artwork to the specified amount"""
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        cart[artwork_id] = quantity
        messages.success(request, f'Updated {artwork.name} quantity to {cart[artwork_id]}')
    else:
        cart.pop(artwork_id)
        messages.success(request, f'Removed {artwork.name} from your cart')

    request.session['shopping_cart'] = cart
    return redirect(reverse('shopping_cart'))

def remove_from_cart(request, artwork_id):
    """Remove the item from the shopping cart"""
    try:
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        cart = request.session.get('shopping_cart', {})
        
        print(f"Cart before removing: {cart}")  # Print the state of the cart
        print(f"Artwork ID to be removed: {artwork_id}")  # Print the artwork id

        if str(artwork_id) in cart:
            cart.pop(str(artwork_id))
            messages.success(request, f'Removed {artwork.name} from your cart')
        else:
            messages.error(request, f'Artwork {artwork.name} is not in the cart')

        print(f"Cart after removing: {cart}")  # Print the state of the cart after removing the artwork
        request.session['shopping_cart'] = cart
        request.session.modified = True

    except Exception as e:
        print(f"Error: {e}")  # Print the exception
        messages.error(request, f'Error removing item: {e}')
    return redirect('shopping_cart')  # Redirect back to the shopping cart