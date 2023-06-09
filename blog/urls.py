from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post_management/', views.post_management, name='post_management'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path(
        'comment/<int:pk>/delete/',
        views.comment_delete,
        name='comment_delete'),
    path('post/create/', views.post_create, name='post_create'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
