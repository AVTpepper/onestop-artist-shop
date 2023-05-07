from django.shortcuts import render
from django.db.models import Q

from artworks.models import Artwork

# Create your views here.


def index(request):
    """ A view to return the index page """
    featured_artworks = Artwork.objects.filter(is_featured=True).order_by('?')[:3]
    request.session['referrer'] = 'home'

    context = {
        'featured_artworks': featured_artworks
    }

    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def faq(request):
    return render(request, 'home/faq.html')