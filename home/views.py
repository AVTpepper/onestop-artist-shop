from django.shortcuts import render
from django.db.models import Q

from artworks.models import Artwork
from blog.models import Post

# Create your views here.


def index(request):
    """ A view to return the index page """
    featured_artworks = Artwork.objects.filter(
        is_featured=True).order_by('?')[:3]
    request.session['referrer'] = 'home'

    context = {
        'featured_artworks': featured_artworks
    }

    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def faq(request):
    return render(request, 'home/faq.html')


def search(request):
    query = request.GET.get('q', '')

    blog_posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query))
    artworks = Artwork.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    )

    context = {
        'blog_posts': blog_posts,
        'artworks': artworks,
        'query': query
    }

    return render(request, 'home/search_results.html', context)
