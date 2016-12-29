currencies = {
    "AUD": "Australian dollar",
    "BGN": "Bulgarian lev",
    "BRL": "Brasilian real",
    "CAD": "Canadian dollar",
    "CHF": "Swiss franc",
    "CNY": "Chinese yuan",
    "CZK": "Czech koruna",
    "DKK": "Danish krone",
    "EUR": "Euro",
    "GBP": "British pound",
    "HKD": "Hong Kong dollar",
    "HRK": "Croatian kuna",
    "HUF": "Hungarian forint",
    "IDR": "Indonesian rupiah",
    "ILS": "Israeli shekel",
    "INR": "Indian rupee",
    "JPY": "Japanese yen",
    "KRW": "South Korean won",
    "MXN": "Mexican peso",
    "MYR": "Malaysian ringgit",
    "NOK": "Norwegian krone",
    "NZD": "New Zealand dollar",
    "PHP": "Philippine peso",
    "PLN": "Polish zloty",
    "RON": "Romanian leu",
    "RUB": "Russian ruble",
    "SEK": "Swedish krona",
    "SGD": "Singapore dollar",
    "THB": "Thai baht",
    "TRY": "Turkish lira",
    "USD": "US dollar",
    "ZAR": "South African rand"
}

def print_rate(value, rate, base, currency):
    print(str(value) + " " + currencies[base] + " = " + str(rate*value) + " " +
            currencies[currency])

def print_help(cmd):
    print(
        "Example: '" + cmd + " 20 USD BRL'\n" +\
        "This converts 20 US dollars to Brazilian reals\n\n" +\
        "Type '" + cmd + " -l' to get all available currencies")

def print_currencies():
    print("Available currencies:\n")
    for k, v in currencies.items():
        print(k, " - ", v)
