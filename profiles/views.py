from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    print("Orders: ", orders)
    for order in orders:
        print("Order number: ", order.order_number)
        print("Line items: ", order.lineitems.all())
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    profile = get_object_or_404(UserProfile, user=request.user)
    order = Order.objects.get(order_number=order_number)
    
    if profile != order.user_profile:
        messages.error(request, (
            'This order does not belong to you.'
        ))
        return redirect(reverse('profile'))

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/complete_order.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)