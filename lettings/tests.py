from django.test import TestCase

from lettings.models import Address, Letting
from django.urls import reverse


class ProfilesIndexViewTest(TestCase):
    def setUp(self):
        # Création des données de test pour la base de données.
        self.address1 = Address.objects.create(
            number="2574",
            street="Beach avenue",
            city="Miami",
            state="FL",
            zip_code=33101,
            country_iso_code="USA",
        )

        self.address2 = Address.objects.create(
            number="1456",
            street="Pine street",
            city="Chicago",
            state="IL",
            zip_code=60614,
            country_iso_code="USA",
        )

        self.letting1 = Letting.objects.create(title="House on the beach", address=self.address1)
        self.letting2 = Letting.objects.create(title="Wooden treehouse", address=self.address2)

    def test_lettings_index_view(self):
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "House on the beach")
        self.assertContains(response, "Wooden treehouse")

    def test_profile_detail_view(self):
        id = self.letting1.id
        address = self.letting1.address
        url = reverse("letting", args=[id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"<p>{address.number} {address.street}</p>")
