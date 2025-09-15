import os
import sys

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Orange Country Lettings"
copyright = "2025, Guillaume Gillon"
author = "Guillaume Gillon"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Ajout du chemin vers le répertoire racine du projet Django
# Cela permet à Django de trouver settings.py
sys.path.insert(0, os.path.abspath("../"))

# Spécifiez le module de paramètres Django
os.environ["DJANGO_SETTINGS_MODULE"] = "oc_lettings_site.settings"
