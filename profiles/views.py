"""
Module des vues pour l'application "Profiles".

Ce module gère l'affichage des pages liées aux profils des utilisateurs.
Il inclut une vue pour afficher la liste de tous les profils et une autre
pour les détails d'un profil spécifique.
"""

from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Vue de la page d'index des profils.

    Affiche une liste de tous les profils d'utilisateurs.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse contenant la page d'index des profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Vue pour la page de détail d'un profil spécifique.

    Affiche les informations d'un profil en fonction du nom d'utilisateur.

    Args:
        request: L'objet HttpRequest.
        username: Le nom d'utilisateur (str) utilisé pour récupérer le profil.

    Returns:
        Un objet HttpResponse contenant la page de détail du profil.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
