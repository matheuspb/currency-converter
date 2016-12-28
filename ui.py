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

def print_rate(rate, base, currency):
    print("1 " + currencies[base] + " = " + str(rate) + " " +
            currencies[currency])

def print_help(cmd):
    print(
        "\n" + cmd + " USD BRL\n" +\
        "This converts from US dollars to Brazilian Reals\n\n" +\
        "'" + cmd + " -l' -> Shows all available currencies\n")

def print_currencies():
    print("Available currencies:\n")
    for k, v in currencies.items():
        print(k, " - ", v)
