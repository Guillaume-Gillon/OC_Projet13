# OC-Projet13 : Mettez à l'échelle une application Django en utilisant une architecture modulaire.

Cette application permet à ses utilisateurs de louer des biens immobiliers.<br>
Il est possible de :<br>
- Lister les profils utilisateurs et accéder aux détails de chaque profil <br>
- Lister les biens et accéder aux détails de chaque bien <br>
<br>

Le projet est disponible publiquement en version stable : [Holiday Homes](https://oc-projet13-latest.onrender.com/)<br>
La documentation complète est disponible sur [Read The Docs](https://gg-oc-projet13.readthedocs.io/fr/latest/index.html)<br>

> [!NOTE]
> Testé sous Ubuntu 24.04 - Python 3.12.3<br>
> Cette documentation est applicable sous cette configuration.<br>
> Les commandes peuvent différer pour d'autres systèmes d'exploitation.

## ✅ Prérequis

Pour installer ce programme, vous aurez besoin d'une connexion internet.<br>
Le programme peut être exécuté en local à des fins de développement.<br>
<br>
Python doit être installé sur votre ordinateur (version 3.12.3 ou supérieur).<br>
<br>
L'installateur **pip** doit également être disponible sur votre machine pour installer les dépendances.
Il est possible d'utiliser **pipenv** pour centraliser la gestion des modules, dépendances et environnement virtuel.

## 📦 Installation et exécution du programme

<details>
<summary>📍 Etape 1 - Installer git</summary><br>

Pour télécharger ce programme, vérifiez que git est bien installé sur votre poste.<br>
Vous pouvez l'installer en suivant les instructions fournies sur le site [git-scm.com](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

</details>

<details>
<summary>📍 Etape 2 - Cloner le dépôt contenant le programme</summary><br>


Placez-vous dans le dossier souhaité et utilisez la commande suivante :

``git clone https://github.com/Guillaume-Gillon/OC_Projet13.git``

</details>

<details>
<summary>📍 Etape 3 - Créer et activer un evironnement virtuel</summary><br>

Créez un environnement virtuel avec la commande<br>
``python3 -m venv env``<br>

Activez cet environnement avec la commande<br>
``source env/bin/activate``

</details>

<details>
<summary>📍 Etape 4 - Installer les dépendances</summary><br>

Pour que ce programme s'exécute, vous aurez besoin de plusieurs packages additionnels listés dans le fichier requirements.txt.<br>

Exécutez la commande <br>
``pip install -r requirements.txt``

</details>

<details>
<summary>📍 Etape 5 - Exécuter l'application</summary><br>

Exécutez les commandes suivantes :<br>
``python3 manage.py collectstatic --noinput``<br>
``RENDER_EXTERNAL_HOSTNAME="127.0.0.1" python3 manage.py runserver``

Ouvrez votre navigateur et tapez dans la barre d'adresse :
``127.0.0.1:8000``

</details>

## ⚙️ Fonctionnement du programme

L'application comporte différentes sections accessibles en cliquant sur les boutons correspondants.
<br>

Il est possible de visiter la liste des profils utilisateurs et des biens disponibles.<br>
En cliquant sur un élément, il est possible d'accéder aux détails de celui-ci.

## 🚀 Exécution des fontionnalités additionnelles

### Tests
Il est possible d'exécuter les jeux de tests.<br>
Activez l'environnement virtuel (voir étape 3 ci-dessus) puis tapez la commande :<br>
``coverage run manage.py test && coverage report``

### Linting

L'outil flake8 est disponible pour vérifier les erreurs de linting.

Activez l'environnement virtuel (voir étape 3 ci-dessus) puis tapez la commande ``flake8``.<br>
Pour créer un fichier de rapport, tapez ``flake8 > flake8_report.txt``

## 🔐 Accès à l'interface d'administration

Il est possible d'accéder à l'interface administrateur de Django.

Exécutez l'application (voir étape 5 ci-dessus) puis accédez à l'adresse ``http://127.0.0.1:8000/admin/``

Entrez le nom d'utilisateur et le mot de passe : admin - Abc1234!

## 💻 Déploiement

Cette section fournit un aperçu de la stratégie de déploiement continu mise en place pour ce projet. Le processus est entièrement automatisé via un workflow GitHub Actions qui assure le bon fonctionnement de la chaîne de déploiement, de la mise à jour du code jusqu'au déploiement sur la plateforme d'hébergement.

### Fonctionnement du déploiement

Le déploiement est orchestré par un workflow GitHub Actions qui suit les étapes suivantes, déclenchées par un push sur la branche main :

    1- Tests unitaires et d'intégration : Le code est d'abord compilé et testé pour s'assurer de sa qualité et de sa fiabilité.

    2- Conteneurisation et publication : Si les tests réussissent, une image Docker est construite et taguée de manière unique avec l'ID du commit. Cette image est ensuite poussée sur Docker Hub. Un second tag, latest, est également appliqué pour indiquer la dernière version stable.

    3- Déclenchement du déploiement : Une fois l'image publiée, le workflow utilise un webhook pour déclencher manuellement un déploiement sur la plateforme Render. Render récupère alors l'image Docker taguée latest et la déploie automatiquement, mettant à jour l'application en production.

Ce processus garantit que seule une version du code validée et testée peut être déployée.

### Configuration requise

Pour que le déploiement fonctionne, les secrets suivants doivent être configurés dans les paramètres du dépôt GitHub (Settings > Secrets and variables > Actions), pour permettre au workflow d'accéder aux services externes :

    DOCKERHUB_USERNAME : Votre nom d'utilisateur Docker Hub.

    DOCKERHUB_TOKEN : Un token d'accès personnel généré sur Docker Hub, avec les droits en lecture et écriture pour votre dépôt Docker.

    RENDER_DEPLOY_HOOK : L'URL du webhook de déploiement fournie par Render, utilisée pour déclencher les déploiements.

### Étapes pour effectuer le déploiement

Le déploiement est un processus automatisé qui ne nécessite aucune intervention manuelle une fois la configuration initiale en place.
Pour mettre à jour l'application en production :

    1- Assurez-vous que toutes vos modifications ont été validées et testées localement.

    2- Créez une Pull Request (PR) pour fusionner vos changements de votre branche de fonctionnalité vers la branche main.

    3- Une fois la PR approuvée, fusionnez-la.

    4- Le workflow GitHub Actions se déclenchera automatiquement sur le push vers la branche main et gérera le processus de déploiement de bout en bout.

Si le déploiement échoue, vérifiez les logs du workflow dans l'onglet Actions de votre dépôt GitHub pour identifier l'étape responsable de l'échec.

Un push sur la branche QA déclenche la compilation et l'exécution des tests.