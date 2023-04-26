from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shopping_cart, name='shopping_cart'),
    path('add/<int:artwork_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('shopping_cart/delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
]
