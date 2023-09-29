# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from datetime import date

# -- Project information -----------------------------------------------------

project = 'PFLOTRAN'
copyright = f'{date.today().year}, www.pflotran.org'
author = ','.join([
    'Benjamin Andre',
    'Gautam Bisht',
    'Nathan Collier',
    'Jennifer Frederick',
    'Glenn Hammond',
    'Piyoosh Jaysaval',
    'Satish Karra',
    'Jitu Kumar',
    'Rosie Leone',
    'Peter Lichter',
    'Chuan Lu',
    'Richard Mills',
    'Michael Nole',
    'Paolo Orsini',
    'Heeho Park',
    'Moise Rousseau',
])

# The full version, including alpha/beta/rc tags
release = 'v5.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx_math_dollar',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'user_guide/cards/process_model_cards/wipp_source_sink*',
]

# output from 
#from pygments.styles import get_all_styles
#styles = list(get_all_styles())
#print(styles)
# ['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 'murphy', 'manni', 'material', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond']

pygments_style = 'sphinx'
#pygments_style = 'sas'
nitpicky = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'alabaster'
html_theme = 'nature'
html_theme_options = {
    'sidebarwidth' : '350',
}
html_logo = '_static/pflotran_logo.jpg' 

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': [
    'globaltoc.html',
    'localtoc.html',
    'relations.html',
    'searchbox.html'
]}

# -- Options for MathJax -----------------------------------------------------
mathjax3_config = {
  'tex': {
    'inlineMath': [['\\(', '\\)']],
    'displayMath': [['\\[', '\\]']],
    'macros': {
      # add latex macros (similar to \def, \newcommand) here and reference in
      # .rst as \porosity
      'porosity': '\phi',
      'saturation': 's',
      'tortuosity': '\tau',
      'density': '\rho',
      'bulkelectricalconductivity': '\sigma',
      'electricalpotential': '\psi',
      # macros for variable units
      'sq': '{^{2}}',
      'cub': '{^{3}}',
      'inv': '{^{-1}}',
      'invsq': '{^{-2}}',
      'invcub': '{^{-3}}',
      'invN': ['{^{-#1}}',1],
      'strnull': '{\\text{-}}',
      'strtime': '{\\text{s}}',
      'strinvtime': '{\strtime\inv}',
      'strlength': '{\\text{m}}',
      'strinvlength': '{\\text{m}\inv}',
      'strarea': '{\strlength\sq}',
      'strinvarea': '{\strlength}\invsq}',
      'strvolume': '{\strlength\cub}',
      'strinvvolume': '{\strlength\invcub}',
      'strmass': '{\\text{kg}}',
      'strinvmass': '{\strmass\inv}',
      'strmol': '{\\text{kmol}}',
      'strinvmol': '{\strmol\inv}',
      'strtemperature': '{\\text{C}}',
      'strinvtemperature': '{\strtemperature\inv}',
      'strenergy': '{\\text{MJ}}',
      'strinvenergy': '{\strenergy\inv}',
      'strpressure': '{\\text{Pa}}',
      'strinvpressure': '{\strpressure\inv}',
      'strviscosity': '{\strmass\,\strinvlength\,\strinvtime}',
      'strinvviscosity': '{\strlength\,\strtime\,\strinvmass}',
      'strvolfrac': ['{\strvolume\,\\text{#1}\,\{\strvolume\,\\text{#2}\}\inv}',2],
      'strporosity': '{\strvolfrac{pore}{bulk}}',
      'strsaturation': ['{\strvolfrac{#1}{pore}}',1],
      'strliquidsaturation': '{\strsaturation{liquid}}',
      'strgassaturation': '{\strsaturation{gas}}',
      'strmassdensity': '{\strmass\,\strinvvolume}',
      'strmoldensity': '{\strmol\,\strinvvolume}',
      'strenergydensity': '{\strenergy\,\strinvvolume}',
      'streleccond': '{\\text{S}\,\strinvlength}',
      'strelecpotential': '{\\text{V}}',
      'strmolfraction': ['{\strmol\,\\text{#1}\,\{\strmol\,\\text{#2}\}\inv}',2],
      'strmassfraction': ['{\strmass\,\\text{#1}\,\{\strmass\,\\text{#2}\}\inv}',2],
      'units':      ['{\\left[{#1}\\right]}',1],
      'unitless':   ['{\\units{\strnull}}'],
      'unitsfrac':  ['{\\left[#1\{#2\}\inv\\right]}',2],
      'unitsfracN': ['{\\left[#1\{#2\}\invN{#3}\\right]}',3],
      'unitsfracstr': ['{\\left[\\text{#1}\{\\text{#2}\}^{-1}\\right]}',2],
      'invstr': ['{\{#1\}^{-#2}}', 2], ## for those macros with arguments
    }
  }
}

