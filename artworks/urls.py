from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path('delete/<int:artwork_id>/', views.delete_artwork, name='delete_artwork'),
]

