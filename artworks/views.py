from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from .models import Artwork, Category
from shopping_cart.forms import AddToCartForm
from .forms import ArtworkEditForm


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

def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def edit_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == 'POST':
        form = ArtworkEditForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', artwork_id=artwork.id)
    else:
        form = ArtworkEditForm(instance=artwork)
    
    context = {'artwork': artwork, 'form': form}

    return render(request, 'artworks/edit_artwork.html')


@user_passes_test(is_staff)
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    artwork.delete()
    return redirect('artworks')