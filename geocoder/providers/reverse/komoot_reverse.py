__all__ = ["KomootReverse"]

import logging

from geocoder.location import Location
from geocoder.providers.addresses import KomootQuery, KomootResult


class KomootReverseResult(KomootResult):
    @property
    def ok(self):
        return bool(self.address)


class KomootReverse(KomootQuery):
    """
    Komoot REST API

    API Reference: http://photon.komoot.de
    """

    _PROVIDER = "komoot"
    _METHOD = "reverse"
    _URL = "https://photon.komoot.de/reverse"
    _RESULT_CLASS = KomootReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            "lat": location.lat,
            "lon": location.lng,
        }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    g = KomootReverse("45.4 -75.7")
    g.debug()
