from django.shortcuts import render
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