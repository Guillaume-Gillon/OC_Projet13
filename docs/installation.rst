============
Installation
============

Pour installer et exécuter le projet en local, suivez les instructions ci-dessous.

#. :ref:`Installer Docker <setup_docker>`
#. :ref:`Cloner l'image Docker <clone_image>`
#. :ref:`Lancer l'application <launch_app>`
#. :ref:`Accéder à l'interface <interface>`

.. note::

    Cette section est applicable sur Windows, MacOS et Linux.

.. _setup_docker:

Installer Docker
----------------

Consulter le `guide d'installation de Docker`_ pour plus d'informations.

.. _guide d'installation de Docker: https://docs.docker.com/get-started/get-docker/

.. _clone_image:

Cloner l'image Docker
---------------------

Pour cloner l'image Docker de l'application, utilisez la commande suivante :

.. code-block:: shell
    
    docker pull guillaumegillon/oc_projet13:latest

.. _launch_app:

Lancer l'application
--------------------

Pour lancer l'application, exécutez la commande suivante :

.. code-block:: shell

    docker run -e RENDER_EXTERNAL_HOSTNAME='127.0.0.1' -p 8080:8000 guillaumegillon/oc_projet13

.. note::
    Le tag -e permet de définir la variable d'environnement RENDER_EXTERNAL_HOSTNAME.
    
    Cette action permet d'autoriser "localhost" à accéder à l'application pour pouvoir l'exécuter sur votre poste.

.. _interface:

Accéder à l'interface
---------------------

Ouvrez votre navigateur et accédez à l'adresse `127.0.0.1:8080 <http://127.0.0.1:8080>`_.