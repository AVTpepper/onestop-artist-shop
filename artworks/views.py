from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import Http404

from .models import Artwork, Category
from shopping_cart.forms import AddToCartForm
from .forms import ArtworkEditForm, AddArtworkForm


# Create your views here.


def all_artworks(request):
    """
    A view to show all artworks, including sorting and search queries.
    """

    artworks = Artwork.objects.all()
    categories = Category.objects.all()
    request.session['referrer'] = 'all_artworks'

    context = {
        'artworks': artworks,
        'categories': categories,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """
    A view to show the detail of an artwork based on the artwork_id.
    """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    form = AddToCartForm(initial={'artwork_id': artwork.id})

    from_home = 'yes' if request.session.get('referrer') == 'home' else 'no'

    context = {
        'artwork': artwork,
        'form': form,
        'from_home': from_home,
    }

    if 'referrer' in request.session:
        del request.session['referrer']

    return render(request, 'artworks/artwork_detail.html', context)


@permission_required('is_staff', raise_exception=True)
def edit_artwork(request, artwork_id):
    """
    A view for editing an existing artwork, accessible only to staff users.
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == 'POST':
        form = ArtworkEditForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', artwork_id=artwork.id)
    else:
        form = ArtworkEditForm(instance=artwork)

    context = {'artwork': artwork, 'form': form}

    return render(request, 'artworks/edit_artwork.html', context)


@permission_required('is_staff', raise_exception=True)
def delete_artwork(request, artwork_id):
    """
    A view for deleting an artwork, accessible only to staff users.
    """
    artwork = get_object_or_404(Artwork, id=artwork_id)
    artwork.delete()

    referrer = request.META.get('HTTP_REFERER', '')

    if 'artwork-management' in referrer:
        return redirect('artwork_management')
    else:
        return redirect('artworks')



@permission_required('is_staff', raise_exception=True)
def artwork_management(request):
    """
    A view for staff users to manage the artworks.
    """
    artworks = Artwork.objects.all()

    context = {'artworks': artworks}
    return render(request, 'artworks/artwork_management.html', context)


@permission_required('is_staff', raise_exception=True)
def add_artwork(request):
    """
    A view for adding a new artwork, accessible only to staff users.
    """
    if request.method == 'POST':
        form = AddArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            return redirect('artwork_detail', artwork_id=artwork.id)
    else:
        form = AddArtworkForm()

    context = {'form': form}
    return render(request, 'artworks/add_artwork.html', context)
