from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=40)
    street_address2 = models.CharField(max_length=40)
    county = models.CharField(max_length=80)

    def __str__(self):
        return f'Order {self.id}'



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    artwork = models.ForeignKey(Artwork, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        and update the order total.
        """
        self.lineitem_total = self.artwork.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.artwork.sku} on order {self.order.order_number}'
