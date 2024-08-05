# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mypage'
copyright = '2024'
author = 'esse LL'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'myst_parser',
	'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['README*', '_build', 'Thumbs.db', '.DS_Store',
                    'jupyter_execute', '*venv*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_title = "My Page"

html_favicon = 'favicon.ico'

html_theme_options = {
    "repository_url": "https://github.com/lacus-w/mypage",
    # "use_repository_button": True,
    "repository_branch": "master",
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
    "show_toc_level": 2,
}
