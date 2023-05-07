from decimal import Decimal
from django.shortcuts import get_object_or_404
from artworks.models import Artwork

def shopping_cart_contents(request):
    """
    Calculate the shopping cart contents and generate a context dictionary with cart items, total, artwork count,
    and grand total. This context can be used in views and templates to display shopping cart information.
    """

    cart_items = []
    total = 0
    artwork_count = 0
    cart = request.session.get('shopping_cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity')
        else:
            quantity = item_data

        artwork = get_object_or_404(Artwork, pk=item_id)
        subtotal = quantity * artwork.price
        total += quantity * artwork.price
        artwork_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork,
            'subtotal': subtotal,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'artwork_count': artwork_count,
        'grand_total': grand_total,
    }

    return context