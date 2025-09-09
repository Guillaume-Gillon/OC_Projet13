"""
Module de configuration pour l'application `profiles`.

Ce module contient la classe de configuration qui permet à Django
de reconnaître et de gérer l'application `profiles`.
"""

from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    """
    Classe de configuration pour l'application `profiles`.

    Gère l'enregistrement et les paramètres de l'application.
    """

    name = "profiles"
