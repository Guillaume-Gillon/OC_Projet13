"""
Module de modèles Django pour les locations immobilières.

Ce module définit les modèles de base pour la gestion des adresses et des biens
à louer. Il inclut les modèles suivants :

- `Address`: Modèle pour la gestion des adresses postales, avec des champs
  spécifiques et des validateurs pour garantir l'intégrité des données.
- `Letting`: Modèle pour les biens à louer, avec une relation one-to-one
  vers une instance d'Address.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle pour les adresses. Chaque adresse contient des informations détaillées
    sur une localisation physique.

    Champs:
    - `number`: Numéro de l'adresse, avec une valeur maximale de 9999.
    - `street`: Nom de la rue, avec une longueur maximale de 64 caractères.
    - `city`: Nom de la ville, avec une longueur maximale de 64 caractères.
    - `state`: Code de l'état (ou de la province), doit avoir 2 caractères.
    - `zip_code`: Code postal, avec une valeur maximale de 99999.
    - `country_iso_code`: Code ISO du pays, doit avoir 3 caractères.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Représentation en chaîne de caractères d'une instance de la classe `Address`.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Modèle représentant un bien immobilier à louer (logement, etc.).
    Chaque bien est lié à une seule adresse.

    Champs:
    - `title`: Le titre ou le nom du bien à louer.
    - `address`: Une relation "one-to-one" vers une instance du modèle `Address`.
                 La suppression d'une adresse entraînera la suppression du bien associé.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Représentation en chaîne de caractères d'une instance de la classe `Letting`.
        """
        return self.title
