from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import OrderLineItem, Order
from shopping_cart.contexts import shopping_cart_contents


def checkout(request):
    cart = shopping_cart_contents(request)
    
    # Debug prints
    print('Cart items:')
    for item in cart['cart_items']:
        print(f'Item ID: {item["item_id"]}, Artwork: {item["artwork"]}')
    # End debug prints

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None            
            order.total = cart['grand_total']
            order.save()
            for item in cart['cart_items']:
                print(item['artwork'])
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
        'cart': cart,
        'form': form,
        'stripe_public_key': 'pk_test_51MoQbkHAS8S3VMAhLOO3X0ZyEzXXIHMYqWS7FoDKzoSKqYTVwom8AvqamgG6kUkhrFpogAFk1UQCfSR71vfratTz00qa1OoAEK',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)


def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'checkout/complete_order.html', context)

