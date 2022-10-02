.. _install:

Installing
==========

*freeplane-python-io* is hosted on PyPI, so installing with `pip` is simple::

    pip install freeplane-io

*freeplane-python-io* depends mainly on the ``lxml`` package. The html parsing is realized
using ``html2text``, which might be replaced by Python's builtin package,
soon. Both ``pip`` and ``easy_install`` will take care of satisfying these
dependencies for you, but if you use the ``setup.py`` installation method
you might need to install the dependencies yourself.

Currently *freeplane-python-io* requires Python 3.3, 3.4, or 3.6 or higher.

Dependencies
------------

* Python 3.3, 3.4, or 3.6 or higher
* lxml
* html2text (to be used for parsing html contents within nodes)