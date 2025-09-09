"""
Module des vues pour l'application "Lettings".

Ce module gère l'affichage des pages liées aux biens immobiliers à louer.
Il inclut les vues pour la liste de tous les biens ainsi que pour les détails
de chaque bien spécifique.
"""

from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Vue pour la page d'index des biens à louer.

    Affiche une liste de tous les biens à louer disponibles.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse contenant la page d'index.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Vue pour la page de détail d'un bien à louer spécifique.

    Affiche les informations d'un bien à louer basé sur son ID.

    Args:
        request: L'objet HttpRequest.
        letting_id: L'identifiant du bien à louer (int).

    Returns:
        Un objet HttpResponse contenant la page de détail du bien.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
