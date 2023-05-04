from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.urls import reverse
from .forms import OrderForm
from .models import OrderLineItem, Order
from artworks.models import Artwork
from shopping_cart.contexts import shopping_cart_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()
    else:
        profile = None

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    current_cart = shopping_cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        metadata={
            'shopping_cart': json.dumps(request.session.get('shopping_cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': str(request.user),
        }
    )

    if request.method == 'POST':
        shopping_cart = request.session.get('shopping_cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        form = OrderForm(form_data)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user if request.user.is_authenticated else None
            order.total = total
            order.save()
            for item in current_cart['cart_items']:
                try:
                    artwork = Artwork.objects.get(id=item['artwork'].id)  # Make sure the artwork exists in DB
                    quantity = item['quantity']
                    lineitem_total = item['subtotal']
                    order_line_item = OrderLineItem(
                        order=order,
                        artwork=artwork,
                        quantity=quantity,
                        lineitem_total=lineitem_total
                    )
                    order_line_item.save()
                except Artwork.DoesNotExist:
                    messages.error(request, (
                        f"The artwork with id {item['artwork'].id} in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_cart'))

            messages.success(request, 'Order successfully placed!')
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('complete_order', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please check your information.')
    else:
        # If this is a GET request, pre-fill the form with the user's default delivery info
        if profile:
            initial_data = {
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            }
        else:
            initial_data = {}
        form = OrderForm(initial=initial_data)

    context = {
        'cart': current_cart,
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'stripe_total': stripe_total,
    }

    return render(request, 'checkout/checkout.html', context)


def complete_order(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)  # Adjust this according to your user model
        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)  # Adjust this according to your user model
            if user_profile_form.is_valid():
                user_profile_form.save()
        
        order.user_profile = profile
        order.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'shopping_cart' in request.session:
        del request.session['shopping_cart']

    template = 'checkout/complete_order.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shopping_cart': json.dumps(request.session.get('shopping_cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

