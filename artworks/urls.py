from django.urls import path
from . import views

# app_name = 'artworks'

# app_name = 'artworks'

urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
]

