#!/usr/bin/env python

import urllib.request, json
from sys import argv

response = urllib.request.urlopen(
        "http://api.fixer.io/latest?base=" + argv[1] +
        "&symbols=" + argv[2])

rates = json.loads(response.read().decode("utf-8"))

print(rates)
