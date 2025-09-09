"""
Module de configuration pour l'application `lettings`.

Ce module contient la classe de configuration de l'application qui permet
à Django de la découvrir et de la configurer correctement.
"""

from django.apps import AppConfig


class LettingAppConfig(AppConfig):
    """
    Classe de configuration pour l'application `lettings`.

    Gère les paramètres de l'application (son nom) pour que Django
    puisse l'identifier et l'enregistrer dans le projet.
    """

    name = "lettings"
