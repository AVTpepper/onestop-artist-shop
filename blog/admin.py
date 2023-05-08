from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'likes_count', 'comments_count')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('author', 'created_at')
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_short', 'author', 'post', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'post__title')
    list_filter = ('author', 'created_at', 'post')
    date_hierarchy = 'created_at'

    def content_short(self, obj):
        return obj.content[:50]
    content_short.admin_order_field = 'content'
    content_short.short_description = 'Content'
