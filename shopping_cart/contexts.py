from decimal import Decimal
from django.shortcuts import get_object_or_404
from artworks.models import Artwork

def shopping_cart_contents(request):

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
        total += quantity * artwork.price
        artwork_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'artwork_count': artwork_count,
        'grand_total': grand_total,
    }

    return context