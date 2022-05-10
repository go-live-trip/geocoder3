

from __future__ import absolute_import

"""
Geocoder
~~~~~~~~

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

"""

__title__ = 'geocoder3'
__author__ = 'Andrey Shpak'
__author_email__ = 'ashpak@ashpak.ru'
__version__ = '2.0.0'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 Andrey Shpak'

# CORE
from geocoder.api import get, yahoo, bing, geonames, mapquest, google, mapbox  # noqa
from geocoder.api import nokia, osm, tomtom, geolytica, arcgis, opencage, locationiq  # noqa
from geocoder.api import maxmind, ipinfo, freegeoip, ottawa, here, baidu, gaode, w3w, ipfinder  # noqa
from geocoder.api import yandex, mapzen, komoot, tamu, geocodefarm, tgos, uscensus  # noqa
from geocoder.api import gisgraphy, geocodexyz # noqa

# EXTRAS
from geocoder.api import timezone, elevation, places, ip, canadapost, reverse, distance, location  # noqa

# CLI
from geocoder.cli import cli  # noqa
