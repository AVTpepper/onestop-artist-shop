from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork
from django_countries.fields import CountryField
from profiles.models import UserProfile


from django.db.models import Sum
import uuid


class Order(models.Model):
    """
    A model to store information about a customer's order.
    This model includes fields for order details, user information,
    shipping address, and payment information.
    The save method is overridden to generate a unique order number,
    and update the total cost.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='orders')
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number,
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model to store information about individual items within an order.
    This model includes fields for the related order, artwork, quantity,
    and line item total.
    The save method is overridden to calculate the line item total,
    and update the order total.
    """
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    artwork = models.ForeignKey(
        Artwork, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        and update the order total.
        """
        self.lineitem_total = self.artwork.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.artwork.sku} on order {self.order.order_number}'
