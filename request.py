import urllib.request
from json import loads

from ui import currencies

def get_rate(base, currency):
    if not base in currencies or not currency in currencies:
        raise KeyError("Currency not available")

    response = urllib.request.urlopen(
            "http://api.fixer.io/latest?base=" + base +
            "&symbols=" + currency)

    response_dict = loads(response.read().decode("utf-8")) # parses json

    return response_dict["rates"][currency]
