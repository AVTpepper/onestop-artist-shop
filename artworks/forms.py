from django import forms
from .models import Artwork

class ArtworkEditForm(forms.ModelForm):
    class Meta:
        model = Artwork
        exclude = ['sku', 'date_created']
