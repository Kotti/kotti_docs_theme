This theme is based on `sphinx-bootstrap`_ by `Scotch Media`_ and modified for
documentation of `Kotti`_ and Kotti add-ons.

How does it look?
-----------------

Visit the `Kotti Documentation`_ to see the theme in action.

How to use
----------

Install from PyPI::

    pip install kotti_docs_theme

Adjust the settings in your Sphinx ``conf.py`` file::

    import kotti_docs_theme

    html_theme_path = [kotti_docs_theme.get_theme_dir()]
    html_theme = 'kotti_docs_theme'
    html_theme_options = {
        'github_user': 'Pylons',
        'github_repo': 'Kotti',
        'twitter_username': 'KottiCMS',
        'home_url': 'http://kotti.pylonsproject.org/',
        'mailing_list_url': 'http://groups.google.com/group/kotti',
        'irc_channel_url': 'irc://irc.freenode.net/#kotti',
    }

Add a rtd.txt file containing the requirements for building the docs on
`Read The Docs`_::

    Sphinx
    kotti_docs_theme
    repoze.sphinx.autointerface
    repoze.lru

.. _sphinx-bootstrap: http://https://github.com/scotch/sphinx-bootstrap
.. _Scotch Media: http://www.scotchmedia.com/
.. _Kotti: http://kotti.pylonsproject.org/
.. _Read The Docs: http://www.readthedocs.org/
.. _Kotti Documentation: http://kotti.readthedocs.org/
