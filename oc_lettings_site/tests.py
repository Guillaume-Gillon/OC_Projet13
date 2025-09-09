from django.test import TestCase
from django.urls import reverse

from bs4 import BeautifulSoup


class ProfilesIndexViewTest(TestCase):

    def test_dummy(self):
        assert 1

    def test_index_view(self):
        """
        Vérifie que la vue de la page d'accueil fonctionne correctement.
        """
        url = reverse("index")
        response = self.client.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        h1_tags = soup.find_all("h1")
        h1_texts = [tag.text.strip() for tag in h1_tags]

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertIn("Welcome to Holiday Homes", h1_texts)

    def test_template_page_not_found(self):
        """
        Vérifie que la vue de la page 404 fonctionne correctement.
        """
        url = reverse("page_404")
        response = self.client.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        h1_tags = soup.find_all("h1")
        h1_texts = [tag.text.strip() for tag in h1_tags]

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "404.html")
        self.assertIn("404 - Page non trouvée", h1_texts)

    def test_template_internal_server_error(self):
        """
        Vérifie que la vue de la page 500 fonctionne correctement.
        """
        url = reverse("page_500")
        response = self.client.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        h1_tags = soup.find_all("h1")
        h1_texts = [tag.text.strip() for tag in h1_tags]

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "500.html")
        self.assertIn("500 - Erreur serveur", h1_texts)

    def test_page_not_found(self):
        response = self.client.get("/unknown_page/", follow=False)
        self.assertEqual(response.status_code, 404)

    def test_internal_server_error(self):
        url = reverse("error_test_500")
        with self.assertRaises(ZeroDivisionError):
            self.client.get(url, follow=False)
