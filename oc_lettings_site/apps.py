"""
Module de configuration pour l'application racine du projet.

Ce module contient la classe de configuration principale qui permet à Django
de reconnaître et de gérer l'application `oc_lettings_site`.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Classe de configuration pour l'application `oc_lettings_site`.

    Gère l'enregistrement et les paramètres de l'application principale du projet.
    """

    name = "oc_lettings_site"
