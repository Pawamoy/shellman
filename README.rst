========
Shellman
========

.. start-badges


|travis|
|codacygrade|
|codacycoverage|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/shellman.svg?branch=master
    :target: https://travis-ci.org/Pawamoy/shellman/
    :alt: Travis-CI Build Status

.. |codacygrade| image:: https://api.codacy.com/project/badge/Grade/85e410da099c46d0bcf3700c563bbc2a
    :target: https://www.codacy.com/app/Pawamoy/shellman/dashboard
    :alt: Codacy Code Quality Status

.. |codacycoverage| image:: https://api.codacy.com/project/badge/Coverage/85e410da099c46d0bcf3700c563bbc2a
    :target: https://www.codacy.com/app/Pawamoy/shellman/dashboard
    :alt: Codacy Code Coverage

.. |pyup| image:: https://pyup.io/repos/github/Pawamoy/shellman/shield.svg
    :target: https://pyup.io/repos/github/Pawamoy/shellman/
    :alt: Updates

.. |version| image:: https://img.shields.io/pypi/v/shellman.svg?style=flat
    :target: https://pypi.python.org/pypi/shellman/
    :alt: PyPI Package latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/shellman.svg?style=flat
    :target: https://pypi.python.org/pypi/shellman/
    :alt: PyPI Wheel

.. |gitter| image:: https://badges.gitter.im/Pawamoy/shellman.svg
    :target: https://gitter.im/Pawamoy/shellman
    :alt: Join the chat at https://gitter.im/Pawamoy/shellman



.. end-badges

Read documentation from comments and render it with templates.

``shellman`` can generate man pages, wiki pages and help text using documentation written
in a shell script's comments.

For example:

.. code:: bash

    #!/bin/bash

    ## \brief Just a demo
    ## \desc This script actually does nothing.

    main() {
      case "$1" in
        ## \option -h, --help
        ## Print this help and exit.
        -h|--help) shellman "$0"; exit 0 ;;
      esac
    }

    ## \usage demo [-h]
    main "$@"


Output when calling ``./demo -h``:

.. code::

    Usage: demo [-h]

    This script actually does nothing.

    Options:
      -h, --help            Print this help and exit.




See http://jinja.pocoo.org/docs/2.10/templates/.

License
=======

Software licensed under `ISC`_ license.

.. _ISC: https://www.isc.org/downloads/software-support-policy/isc-license/

Installation
============

::

    [sudo -H] pip install shellman

Development
===========

To run all the tests: ``tox``

Usage
=====

