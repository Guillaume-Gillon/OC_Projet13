"""
Module de modèles Django pour les profils utilisateurs.

Ce module définit le modèle `Profile` pour étendre les informations du modèle
`User` de Django et ainsi stocker des données additionnelles.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle de profil utilisateur qui étend le modèle User de Django.
    Chaque utilisateur a un profil unique pour stocker des informations additionnelles.

    Champs:
    - `user`: Une relation "one-to-one" vers le modèle User. La suppression d'un
              utilisateur entraîne la suppression de son profil.
              L'argument `related_name` permet un accès direct depuis le modèle
              User, par exemple : `user.profiles_profile`.
    - `favorite_city`: La ville favorite de l'utilisateur. Ce champ peut être vide.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles_profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Représentation en chaîne de caractères du profil.
        Retourne le nom d'utilisateur associé.
        """
        return self.user.username
