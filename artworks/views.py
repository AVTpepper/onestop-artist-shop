from django.shortcuts import render, get_object_or_404
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


def artwork_detail(request, artwork_id):

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})
