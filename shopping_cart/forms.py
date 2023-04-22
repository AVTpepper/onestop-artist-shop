from django import forms
from artworks.models import Artwork


class AddToCartForm(forms.Form):
    artwork_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1, initial=1, label="Quantity")
