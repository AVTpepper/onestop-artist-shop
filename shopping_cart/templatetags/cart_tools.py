from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity