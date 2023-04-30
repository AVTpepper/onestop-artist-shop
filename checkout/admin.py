from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date_ordered',
                       'total',
                       'stripe_pid')

    fields = ('order_number', 'user', 'date_ordered', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'total',
              'stripe_pid')

    list_display = ('order_number', 'date_ordered', 'full_name',
                    'total',)

    ordering = ('-date_ordered',)

admin.site.register(Order, OrderAdmin)