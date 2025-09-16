"""
Module des vues de base pour le site web.

Ce module contient les vues de la page d'accueil ainsi que les vues personnalisées
pour gérer les erreurs 404 (Page non trouvée) et 500 (Erreur serveur).
"""

from django.shortcuts import render
from django.http import Http404, HttpResponse

import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Vue de la page d'accueil.

    Affiche la page d'accueil de l'application.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse contenant la page d'accueil.
    """
    return render(request, "index.html")


def page_not_found(request):
    """
    Vue personnalisée pour les erreurs 404 (Page non trouvée).

    Cette vue lève une exception Http404, ce qui force Django à afficher la page
    d'erreur 404.html.

    Args:
        request: L'objet HttpRequest.

    Raises:
        Http404: Toujours levée pour simuler une erreur de page non trouvée.
    """
    logger.error("Page d'erreur 404 appelée.")
    raise Http404  # pragma: no cover


def server_error(request):
    """
    Vue personnalisée pour les erreurs 500 (Erreur serveur).

    Cette vue provoque une erreur de code (division par zéro) pour simuler
    une erreur de serveur interne.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Cette fonction ne retourne pas de réponse normale,
                      elle génère une erreur.
    """
    return HttpResponse(1 / 0)
