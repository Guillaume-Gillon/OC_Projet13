===========================
Interfaces de programmation
===========================

* :ref:`Les URLs <urls_interface>`
* :ref:`Les applications <apps_interface>`
* :ref:`Les templates <templates_interface>`
* :ref:`Les fichiers statiques <statics_interface>`
* :ref:`Les APIs <apis_interface>`

.. _urls_interface:

Les URLs
--------

* **Page d'accueil**

    - **URL** : */*
    - **Vue** : *views.index*
    - **Description** : Affiche la page d'accueil. Point d'entrée principal pour les utilisateurs.

* **Pages des locations**

    + **Tous les éléments**
        - **URL** : */lettings/*
        - **Vue** : *lt_views.lettings_index*
        - **Description** : Mène à la page d'index qui liste toutes les locations disponibles.

    + **Détail d'un élément**
        - **URL** : */lettings/<int:letting_id>/*
        - **Vue** : *lt_views.letting*
        - **Description** : Affiche les détails d'une location spécifique. <int:letting_id> est un paramètre qui capture l'identifiant numérique de la location.

* **Pages des profils**

    + **Tous les éléments**
        - **URL** : */profiles/*
        - **Vue** : *pf_views.profiles_index*
        - **Description** : Mène à la page d'index qui liste tous les profils d'utilisateurs.

    + **Détail d'un élément**
        - **URL** : */profiles/<str:username>/*
        - **Vue** : *pf_views.profile*
        - **Description** : Affiche le profil d'un utilisateur spécifique. <str:username> est un paramètre qui capture le nom d'utilisateur.

* **Page de gestion**

    - **URL** : */admin/*
    - **Vue** : *admin.site.urls*
    - **Description** : Fournit l'accès à l'interface d'administration de Django, qui permet de gérer les données de l'application.

* **Pages d'erreur**

    + **404**
        - **URL** : */page-404/*
        - **Vue** : *TemplateView.as_view(template_name="404.html")*
        - **Description** : Affiche une page d'erreur standard pour les ressources non trouvées.

    + **500**
        - **URL** : */page-500/*
        - **Vue** : *TemplateView.as_view(template_name="500.html")*
        - **Description** : Affiche une page d'erreur standard pour les erreurs internes du serveur.

    + **500 (tests)**
        - **URL** : */error-test-500/*
        - **Vue** : *views.server_error*
        - **Description** : Sert de point de test pour déclencher une erreur 500 et vérifier l'affichage de la page d'erreur correspondante.

.. _apps_interface:

Les applications
----------------

* **lettings**

Cette application contient les vues, les fichiers statiques, les modèles et les templates de la section des biens disponibles.

* **profiles**

Cette application contient les vues, les fichiers statiques, les modèles et les templates de la section des profils utilisateurs.

* **oc_lettings_site (application principale)**

C'est l'application principale du projet Django. Elle centralise les configurations globales et les paramètres communs à toutes les autres applications.

Elle contient :

    - Les paramètres de configuration (*'settings.py'*).
    - Les configurations d'URL (*'urls.py'*).
    - Les vues pour les pages principales, comme la page d'accueil (*'index.html'*), et les pages d'erreurs.
    - Les tests liés à la page d'accueil et aux pages d'erreur (*'404.html'* et *'500.html'*).
    - Le template de base qui est étendu par les autres applications.
    - L'interface d'administration.

.. _templates_interface:

Les templates
-------------

Chaque application (*lettings* et *profiles*) possède son propre ensemble de templates spécifiques à ses vues.

Cependant, les templates globaux sont stockés dans le répertoire *'templates/'* à la racine du projet. Ce répertoire contient :

    - Le template de base (*'base.html'*), qui sert de squelette et est étendu par les autres templates pour garantir une mise en page uniforme sur l'ensemble du site.
    - Les templates des pages d'erreur standard de Django, à savoir la page 404 (non trouvée) et la page 500 (erreur serveur).
    - Le template de la page d'accueil (*'index.html'*), qui est servi par l'application principale.

.. _statics_interface:

Les fichiers statiques
----------------------

Les fichiers statiques sont centralisés dans le répertoire *'static/'*' à la racine du projet. Ce répertoire contient tous les fichiers non générés par l'application, tels que :

    - Les fichiers *CSS* pour le style global.
    - Les fichiers *JavaScript* (JS) pour les scripts côté client.
    - Les *assets* du projet, incluant les images, les polices, etc.

Le serveur utilise un middleware comme `whitenoise <https://pypi.org/project/whitenoise/6.9.0/>`_ pour servir ces fichiers efficacement en production, garantissant ainsi de bonnes performances.

.. _apis_interface:

Les APIs
--------

L'application présentée ne met pas de points de terminaison RESTful à disposition des développeurs.
