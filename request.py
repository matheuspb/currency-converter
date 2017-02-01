import urllib.request
from json import loads

from ui import currencies

def get_rate(base, target):
    if not base in currencies or not target in currencies:
        raise KeyError("Currency not available")

    try:
        response = urllib.request.urlopen(
                "http://api.fixer.io/latest?base=" + base +
                "&symbols=" + target)
    except:
        raise RuntimeError("request failed")
    else:
        response_dict = loads(response.read().decode("utf-8")) # parses json
        return response_dict["rates"][target]
