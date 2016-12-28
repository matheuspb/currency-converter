import urllib.request, json

response = urllib.request.urlopen("http://api.fixer.io/latest?base=USD")

rates = json.loads(response.read().decode("utf-8"))

print(rates["rates"]["BRL"])
