========================
Technologies et langages
========================

Pour installer le projet en local, suivez les instructions ci-dessous.

#. :ref:`Langage et modules <language>`
#. :ref:`Disponibilité du code source <source_code>`
#. :ref:`Conteneurisation <contener>`
#. :ref:`Hébergement <hosting>`

.. _language:

Langage et modules
------------------

L'application a été écrite en Python (3.12.3) sur le framework Django (5.2.6) avec une base de données `SQLite <https://sqlite.org/index.html>`_.
Les modules suivants ont été utilisés :

- `pytest <https://pypi.org/project/pytest/8.4.2/>`_, `pytest-django <https://pypi.org/project/pytest-django/4.11.1/>`_ et `beautifulsoup4 <https://pypi.org/project/beautifulsoup4/4.13.5/>`_ pour les tests
- `coverage <https://pypi.org/project/coverage/7.10.6/>`_ pour mesurer la couverture de tests
- `flake8 <https://pypi.org/project/flake8/6.1.0/>`_ et `flake8-django <https://pypi.org/project/flake8-django/1.4/>`_ pour générer le rapport de linting
- `whitenoise <https://pypi.org/project/whitenoise/6.9.0/>`_ pour servir les fichiers statiques
- `gunicorn <https://pypi.org/project/gunicorn/23.0.0>`_ pour servir l'application en production

.. _source_code:

Disponibilité du code source
----------------------------

Le code source de l'application est `hébergé sur GitHub <https://github.com/Guillaume-Gillon/OC_Projet13.git>`_.

Un workflow GitHub Actions est mis en place permettant lors de chaque commit sur la branche main :

* L'exécution des jeux de tests intégrés à l'application
* La mise à jour de l'image conteneurisée
* Le déploiement du conteneur chez l'hébergeur


.. _contener:

Conteneurisation
----------------

L'application conteneurisée via Docker est disponible sur `Docker Hub <https://hub.docker.com/r/guillaumegillon/oc_projet13>`_.

.. _hosting:

Hébergement
-----------

L'application est déployée et hébergée via Render.

`Cliquez ici <https://oc-projet13-latest.onrender.com/>`_ pour accéder au site web public.