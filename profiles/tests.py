from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


class ProfilesIndexViewTest(TestCase):
    def setUp(self):
        # Création des données de test pour la base de données.
        self.user1 = User.objects.create(
            username="JohnDoe", first_name="John", last_name="Doe", email="johndoe@test.com"
        )
        Profile.objects.create(user=self.user1, favorite_city="New York")

        self.user2 = User.objects.create(
            username="JaneDoe", first_name="Jane", last_name="Doe", email="janedoe@test.com"
        )
        Profile.objects.create(user=self.user2, favorite_city="Paris")

    def test_profiles_index_view(self):
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JohnDoe")
        self.assertContains(response, "JaneDoe")

    def test_profile_detail_view(self):
        username = self.user1.username
        first_name = self.user1.first_name
        url = reverse("profile", args=[username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"<p><strong>First name :</strong> {first_name}</p>")
