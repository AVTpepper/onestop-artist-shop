from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shopping_cart, name='shopping_cart'),
    path('add/<int:artwork_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<int:artwork_id>/', views.adjust_cart, name='adjust_cart'),
    path(
        'remove/<int:artwork_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
]
