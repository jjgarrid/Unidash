# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Unidash'
author = 'Author Name'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
