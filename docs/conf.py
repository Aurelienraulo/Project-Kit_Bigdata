"""Initialize documentation Sphinx."""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Informations sur le projet -----------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Projet-Kit_Bigdata'
copyright = '2023, Alban Pereira - Yuchen Xia - Aurélien Raulo - Salimatou Traore'
author = 'Alban Pereira at alban.pereira@telecom-paris.fr - Yuchen Xia at yuchen.xia@telecom-paris.fr \
    - Aurélien Raulo at aurelien.raulo@telecom-paris.fr - Salimatou Traore at salimatou.traore@telecom-paris.fr'
release = '1.0.0'

# -- Configuration générale ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']

templates_path = ['furo']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options pour la sortie HTML -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
