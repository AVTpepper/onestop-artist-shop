from django.shortcuts import render
from .models import Artwork, Category


# Create your views here.


def all_artworks(request):
    """ A view to show all products, including sorting and search queries """

    artworks = Artwork.objects.all()
    category = Category.objects.all()

    context = {
        'artworks': artworks,
        'categories': category,
    }

    return render(request, 'artworks/artworks.html', context)
