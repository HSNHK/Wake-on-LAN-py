#########
wake on lan python
#########


.. image:: https://img.shields.io/pypi/pyversions/wakeonlan.svg
   :target: https://pypi.org/project/wakeonlan/#files
   :alt: Supported Python versions

.. image:: https://img.shields.io/travis/remcohaszing/pywakeonlan/master.svg
    :target: https://travis-ci.org/remcohaszing/pywakeonlan
    :alt: Build Status

.. image:: https://readthedocs.org/projects/pywakeonlan/badge/?version=latest
    :target: https://pywakeonlan.readthedocs.io/en/latest
    :alt: Documentation Status

.. image:: https://codecov.io/gh/remcohaszing/pywakeonlan/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/remcohaszing/pywakeonlan
   :alt: Code coverage

A small python module for wake on lan.

For more information on the wake on lan protocol please take a look at
Wikipedia_.


*****
Usage
*****

To wake up a computer using wake on lan it must first be enabled in the BIOS
settings. Please note the computer you are trying to power on does not have an
ip address, but it does have a mac address. The package needs to be sent as a
broadcast package.



- Python3.x


*******
License
*******

MIT


.. _GitHub: https://github.com/HSNHK/Wake-on-LAN-py.git
.. _Wikipedia: http://en.wikipedia.org/wiki/Wake-on-LAN
