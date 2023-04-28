from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('complete_order/', views.complete_order, name='complete_order'),
]
