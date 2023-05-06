from django import forms
from .models import Artwork

class ArtworkEditForm(forms.ModelForm):
    class Meta:
        model = Artwork
        exclude = ['sku', 'date_created']


class AddArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        exclude = ['date_created', 'rating', 'sku']
