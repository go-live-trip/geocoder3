__all__ = ["FreeGeoIPQuery"]

import logging

import ratelim
import requests

from geocoder.base import MultipleResultsQuery, OneResult


class FreeGeoIPResult(OneResult):
    @property
    def lat(self):
        return self.raw_json.get("latitude")

    @property
    def lng(self):
        return self.raw_json.get("longitude")

    @property
    def address(self):
        if self.city:
            return "{0}, {1} {2}".format(self.city, self.state, self.country)
        elif self.state:
            return "{0}, {1}".format(self.state, self.country)
        elif self.country:
            return "{0}".format(self.country)
        return ""

    @property
    def postal(self):
        zip_code = self.raw_json.get("zip_code")
        postal_code = self.raw_json.get("postal_code")
        if zip_code:
            return zip_code
        if postal_code:
            return postal_code

    @property
    def city(self):
        return self.raw_json.get("city")

    @property
    def state(self):
        return self.raw_json.get("region")

    @property
    def region_code(self):
        return self.raw_json.get("region_code")

    @property
    def country(self):
        return self.raw_json.get("country_name")

    @property
    def country_code3(self):
        return self.raw_json.get("country_code3")

    @property
    def continent(self):
        return self.raw_json.get("continent")

    @property
    def timezone(self):
        return self.raw_json.get("timezone")

    @property
    def area_code(self):
        return self.raw_json.get("area_code")

    @property
    def dma_code(self):
        return self.raw_json.get("dma_code")

    @property
    def offset(self):
        return self.raw_json.get("offset")

    @property
    def organization(self):
        return self.raw_json.get("organization")

    @property
    def ip(self):
        return self.raw_json.get("ip")

    @property
    def time_zone(self):
        return self.raw_json.get("time_zone")


class FreeGeoIPQuery(MultipleResultsQuery):
    """
    FreeGeoIP.live

    freegeoip.live provides a public HTTP API for software developers to
    search the geolocation of IP addresses. It uses a database of IP addresses
    that are associated to cities along with other relevant information like
    time zone, latitude and longitude.

    You're allowed up to 10,000 queries per hour by default. Once this
    limit is reached, all of your requests will result in HTTP 403,
    forbidden, until your quota is cleared.

    API Reference: https://freegeoip.live/
    """

    provider = "freegeoip"
    method = "geocode"

    _URL = "https://freegeoip.live/json/"
    _RESULT_CLASS = FreeGeoIPResult
    _KEY_MANDATORY = False

    def _before_initialize(self, location, **kwargs):
        self.url += location

    @staticmethod
    @ratelim.greedy(10000, 60 * 60)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    g = FreeGeoIPQuery("99.240.181.199")
    g.debug()
