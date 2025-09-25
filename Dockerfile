# On utilise la version 3.12.3-slim, basée sur Debian.
# L'image "slim" est plus petite et ne contient que les paquets essentiels, ce qui réduit la taille finale et les vulnérabilités.
FROM python:3.12.3-slim

# Permet un accès plus direct aux journaux de logs (docker logs)
ENV PYTHONUNBUFFERED=1

# Empêche l'application de créer les __pycache__ pour optimiser la taille du conteneur.
ENV PYTHONDONTWRITEBYTECODE=1

# Crée un dossier "app" et le définit comme répertoire de travail. Toutes les commandes suivantes seront exécutées depuis ce dossier.
WORKDIR /app

# Installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le code de votre répertoire local dans le conteneur.
COPY . .

# Crée le dossier staticfiles qui permet à gunicorn de servir les statiques.
RUN python manage.py collectstatic --noinput

# Expose le port 8000
# Mapper ce port lors de l'exécution du conteneur (`-p 8080:8000`).
EXPOSE 8000

# Définit la commande par défaut qui sera exécutée au démarrage du conteneur.
# Ici, on lance le serveur gunicorn.
# L'adresse 0.0.0.0 est nécessaire pour que le serveur soit accessible depuis l'extérieur du conteneur.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi"]
