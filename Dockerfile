# 1. Image de base
# On utilise la version 3.12.3-slim, basée sur Debian. L'image "slim" est plus petite et ne contient que les paquets essentiels, ce qui réduit la taille finale de votre image et les vulnérabilités.
FROM python:3.12.3-slim

# 2. Variables d'environnement
# Ces variables de configuration sont souvent recommandées pour optimiser les performances et la journalisation de Python dans un conteneur.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 3. Répertoire de travail
# Crée un dossier "app" et le définit comme répertoire de travail. Toutes les commandes suivantes seront exécutées depuis ce dossier.
WORKDIR /app

# 4. Installation des dépendances
# Copie le fichier requirements.txt pour installer les dépendances avant de copier le code de l'application.
# Cela permet à Docker de mettre en cache cette étape. Si vous ne modifiez pas les dépendances, la prochaine construction sera beaucoup plus rapide.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie du code de l'application
# Copie tout le code de votre répertoire local dans le conteneur.
COPY . .

RUN python manage.py collectstatic --noinput

# 6. Exposer le port
# Informe Docker qu'une application écoute sur le port 8000 à l'intérieur du conteneur.
# N'oubliez pas de mapper ce port lors de l'exécution du conteneur (`-p 8080:8000`).
EXPOSE 8000

# 7. Commande de démarrage
# Définit la commande par défaut qui sera exécutée au démarrage du conteneur.
# Ici, on lance le serveur de développement Django. L'adresse 0.0.0.0 est nécessaire pour que le serveur soit accessible depuis l'extérieur du conteneur.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]
