# OC-Projet13 : Mettez à l'échelle une application Django en utilisant une architecture modulaire.

Cette application permet à ses utilisateurs de louer des biens immobiliers.<br>
Il est possible de :<br>
- Lister les profils utilisateurs et accéder aux détails de chaque profil <br>
- Lister les biens et accéder aux détails de chaque bien <br>
<br>

Le projet est disponible publiquement en version stable : [Holiday Homes](https://oc-projet13-latest.onrender.com/)<br>
La documentation complète est disponible sur [Read The Docs](https://gg-oc-projet13.readthedocs.io/fr/latest/index.html)<br>

> [!NOTE]
> Testé sous Ubuntu 24.04 - Python 3.12.3
> Cette documentation est applicable sous cette configuration.
> Les commandes peuvent différer sour un autre OS.

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
``python manage.py collectstatic --noinputut``<br>
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

## 🛠️ Accès à l'interface d'administration

Il est possible d'accéder à l'interface administrateur de Django.

Exécutez l'application (voir étape 5 ci-dessus) puis accédez à l'adresse ``http://127.0.0.1:8000/admin/``

Entrez le nom d'utilisateur et le mot de passe : admin - Abc1234!