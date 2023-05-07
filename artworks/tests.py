from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Artwork

# Create your tests here.


class ArtworkModelTests(TestCase):

    def test_artwork_creation(self):
        """
        Test the creation of an Artwork instance.
        """
        artwork = Artwork.objects.create(
            name="Test Artwork", description="Test description", price=10)
        self.assertEqual(artwork.name, "Test Artwork")
        self.assertEqual(artwork.description, "Test description")
        self.assertEqual(artwork.price, 10)


class ArtworkViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.artwork = Artwork.objects.create(
            name="Test Artwork", description="Test description", price=10)

    def test_view_artwork_detail(self):
        """
        Test the artwork detail view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('artwork_detail', args=[str(self.artwork.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Artwork")
        self.assertContains(response, "Test description")
        self.assertContains(response, "10")
