from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_OTNNSU10nIEQUyy3qqyKYnNLvkoabF3d6Hxp7jZk"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url).json()
    return response['data']

def print_currencies(currencies):
    for currency, value in currencies.items():
        print(str(currency))

def exchange_rate(currency1, currency2, data):
    value1 = data[currency1]
    value2 = data[currency2]
    return value2 / value1

def convert(currency1, currency2, amount, data):
    rate = exchange_rate(currency1, currency2, data)
    
    try: 
        amount = float(amount)
    except: 
        print("Invalid amount") 
        return 
    
    converted_amount = rate * amount
    print(str(amount) + " " + str(currency1) + " is equal to " + str(converted_amount) + " " + str(currency2))

def main():
    data = get_currencies()

    print("Welcome to the Currency Converter")
    print("List- lists the different currencies")
    print("Convert- convert from one currency to another currency")
    print("Exchange- get the exchange rate between two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == 'q':
            break

        if command == 'list':
            print_currencies(data)
        elif command == 'convert':
            currency1 = input("Enter a base currency id: ").upper()
            amount = input("Enter an amount in " + str(currency1) + ": ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount, data)
        elif command == 'exchange':
            currency1 = input("Enter a base currency id: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            value = exchange_rate(currency1, currency2, data)
            print("The exchange rate between the two currencies is: " + str(value))
        else:
            print("Unrecognized Command. Try Again")

main()