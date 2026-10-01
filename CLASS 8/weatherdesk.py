"""
weatherdesk - gives you the live weather above any city in the world.

You do not need to read or change this file. You only need to use it:

    import weatherdesk

    temp, rain = weatherdesk.weather_now("Mumbai")

The function asks a free weather service called Open-Meteo for the latest
reading, so your program talks to a computer on the internet every time you
call it and you need a working internet connection.

If the city name cannot be found, or the internet is not reachable, both
values come back as -1.0. Your program should treat -1.0 as "no data".
"""

import json
import urllib.parse
import urllib.request


def _find_city(city):
    """Convert a city name into its latitude and longitude.

    The weather service does not understand names like "Mumbai". It only
    understands coordinates. So we first ask its geocoding service to look
    the name up for us. This is an API call: we build a web address, send
    it over the internet, and read back the answer.

    Returns (latitude, longitude), or None if the city was not found.
    """
    url = ("https://geocoding-api.open-meteo.com/v1/search?count=1&name="
           + urllib.parse.quote(city))

    # urlopen sends the request over the internet and gives back the reply.
    # The reply is text in a format called JSON, which json.load turns into
    # a normal Python dictionary.
    response = urllib.request.urlopen(url, timeout=20)
    data = json.load(response)

    results = data.get("results")
    if not results:
        return None

    first = results[0]
    return float(first["latitude"]), float(first["longitude"])


def _weather_now(city):
    """Ask the weather service for the current reading above a city.

    Returns (temperature_in_celsius, rain_in_mm).
    Returns (-1.0, -1.0) if anything goes wrong.
    """
    # Networks hiccup. If the first attempt fails, try once more before
    # giving up, so one bad moment does not look like a broken program.
    for attempt in (1, 2):
        result = _try_once(city)
        if result is not None:
            return result
    return -1.0, -1.0


def _try_once(city):
    """One attempt. Returns (temp, rain), or None if it did not work."""
    try:
        place = _find_city(city)
        if place is None:
            return -1.0, -1.0   # the name is genuinely unknown

        latitude, longitude = place

        # Second API call: now that we have the coordinates, ask for the
        # current temperature and rainfall at that exact spot.
        url = ("https://api.open-meteo.com/v1/forecast"
               "?latitude=" + str(latitude) +
               "&longitude=" + str(longitude) +
               "&current=temperature_2m,rain")

        response = urllib.request.urlopen(url, timeout=20)
        data = json.load(response)

        current = data["current"]
        return float(current["temperature_2m"]), float(current["rain"])

    except Exception:
        # Anything can go wrong on a network: no Wi-Fi, the service is busy,
        # an unexpected reply. We do not crash the student's program; we
        # report failure so the caller can try again or give up.
        return None


def weather_now(city):
    """Current weather above `city`.

    Returns two values: the temperature in Celsius and the rainfall in
    millimetres. Use it like this:

        temp, rain = weatherdesk.weather_now("Mumbai")

    Both values are -1.0 if the city was not found or the internet could
    not be reached.
    """
    return _weather_now(city)