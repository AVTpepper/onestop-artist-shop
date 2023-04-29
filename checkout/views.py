from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import OrderLineItem, Order
from shopping_cart.contexts import shopping_cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    current_cart = shopping_cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total = total
            order.save()
            for item in current_cart['cart_items']:
                OrderLineItem.objects.create(
                    order=order,
                    artwork=item['artwork'],
                    quantity=item['quantity'],
                    lineitem_total=item['subtotal']
                )
            messages.success(request, 'Order successfully placed!')
            return redirect('complete_order', order_id=order.id)
        else:
            messages.error(request, 'There was an error with your form. Please check your information.')
    else:
        form = OrderForm()

    context = {
        'cart': current_cart,
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'stripe_total': stripe_total,
    }

    return render(request, 'checkout/checkout.html', context)


def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'checkout/complete_order.html', context)
