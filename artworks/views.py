from django.shortcuts import render, get_object_or_404

from .models import Artwork, Category
from shopping_cart.forms import AddToCartForm


# Create your views here.


def all_artworks(request):
    """ A view to show all products, including sorting and search queries """

    artworks = Artwork.objects.all()
    categories = Category.objects.all()

    context = {
        'artworks': artworks,
        'categories': categories,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    
    # Create an instance of the AddToCartForm and set the artwork_id
    form = AddToCartForm(initial={'artwork_id': artwork.id})

    # Update the context to include the form
    context = {'artwork': artwork, 'form': form}

    return render(request, 'artworks/artwork_detail.html', context)
