from django.db import models
from django.contrib.auth.models import User
from artworks.models import Artwork


class CartItem(models.Model):
    """
    A model representing a cart item, linking a user, an artwork,
    and a quantity.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.artwork.name} ({self.quantity}) - {self.user.username}"
