from django import forms
from .models import Artwork

class ArtworkEditForm(forms.ModelForm):
    """
    ArtworkEditForm is a form used for editing an existing Artwork instance.
    The fields 'sku' and 'date_created' are excluded from the form.
    """
    class Meta:
        model = Artwork
        exclude = ['sku', 'date_created']


class AddArtworkForm(forms.ModelForm):
    """
    AddArtworkForm is a form used for creating a new Artwork instance.
    The fields 'date_created', 'rating', and 'sku' are excluded from the form.
    """
    class Meta:
        model = Artwork
        exclude = ['date_created', 'rating', 'sku']
