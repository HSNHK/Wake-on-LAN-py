#########
wake on lan python
#########


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
simple packet
*******
create the magic packet from MAC address :

\xff\xff\xff\xff\xff\xff\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"
3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"
3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU\x00\x11"3DU

*******
License
*******

MIT


.. _GitHub: https://github.com/HSNHK/Wake-on-LAN-py.git
.. _Wikipedia: http://en.wikipedia.org/wiki/Wake-on-LAN
