from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    A form for creating and editing comments.
    """
    class Meta:
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    """
    A form for creating and editing posts.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
