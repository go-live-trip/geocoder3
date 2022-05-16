__all__ = ["GoogleTimezone"]

import time

from geocoder.base import MultipleResultsQuery, OneResult
from geocoder.keys import google_key
from geocoder.location import Location


class GoogleTimezoneResult(OneResult):
    def __repr__(self):
        return "<[{}] [{}]>".format(self.status, self.timeZoneName)

    @property
    def ok(self):
        return bool(self.timeZoneName)

    @property
    def timeZoneId(self):
        return self.raw_json.get("timeZoneId")

    @property
    def timeZoneName(self):
        return self.raw_json.get("timeZoneName")

    @property
    def rawOffset(self):
        return self.raw_json.get("rawOffset")

    @property
    def dstOffset(self):
        return self.raw_json.get("dstOffset")


class GoogleTimezone(MultipleResultsQuery):
    """
    Google Time Zone API

    The Time Zone API provides time offset data for locations on the surface of the
    earth.
    Requesting the time zone information for a specific Latitude/Longitude pair will
    return the name of that time zone, the time offset from UTC, and the Daylight
    Savings offset.

    API Reference: https://developers.google.com/maps/documentation/timezone/
    """

    provider = "google"
    method = "timezone"

    _URL = "https://maps.googleapis.com/maps/api/timezone/json"
    _RESULT_CLASS = GoogleTimezoneResult
    _KEY = google_key

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            # required
            "key": provider_key,
            "location": str(Location(location)),
            "timestamp": kwargs.get("timestamp", time.time()),
        }

        return params

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == "__main__":
    g = GoogleTimezone([45.5375801, -75.2465979])
    g.debug()
