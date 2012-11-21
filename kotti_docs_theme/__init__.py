# -*- coding: utf-8 -*-

import os


def get_theme_dir():
    """Returns path to directory containing this package's Sphinx themes.

    This is designed to be used when setting the ``html_theme_path``
    option within Sphinx's ``conf.py`` file.
    """

    _root_dir = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(_root_dir, "themes")
