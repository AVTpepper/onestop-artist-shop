from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A model representing a blog post, containing a title, content,
    creation and update timestamps, an author, and an image.
    """
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', default='posts/default.png')

    def __str__(self):
        return self.title
    
    def likes_count(self):
        return self.likes.count()

    def comments_count(self):
        return self.comments.count()


class Comment(models.Model):
    """
    A model representing a comment on a blog post, containing the content,
    creation and update timestamps, an author, and a reference to the post.
    """
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]
    
    def is_author(self, user):
        return self.author == user


class Like(models.Model):
    """
    A model representing a like on a blog post, containing a user and a reference to the post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
