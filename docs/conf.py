# Archivo de configuración para el generador de documentación Sphinx.

# -- Información del proyecto -----------------------------------------------------

project = 'Unidash'
author = 'Nombre del Autor'

# -- Configuración general ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Opciones para la salida HTML -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
