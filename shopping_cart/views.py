from django.shortcuts import render, redirect, get_object_or_404
from shopping_cart.forms import AddToCartForm
from artworks.models import Artwork
from .models import CartItem


def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    # Retrieve the cart items associated with the current user
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the subtotal for each item
    # for item in cart_items:
    #     item.subtotal = item.artwork.price * item.quantity

    # Pass the cart_items variable as context to the template
    context = {'cart_items': cart_items}

    return render(request, 'shopping_cart/cart.html', context)


def add_to_cart(request, artwork_id):
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        if form.is_valid():
            artwork_id = form.cleaned_data['artwork_id']
            quantity = form.cleaned_data['quantity']
            artwork = get_object_or_404(Artwork, id=artwork_id)
            user = request.user

            # Check if the item is already in the cart
            cart_item, created = CartItem.objects.get_or_create(
                artwork=artwork,
                user=user,
                defaults={'quantity': quantity},
            )

            # If the item is already in the cart, update the quantity
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            # Redirect the user to the shopping cart page
            return redirect('shopping_cart')

    # If the request is not POST or the form is not valid, redirect to the home page
    return redirect('home')