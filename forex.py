"""Utilities related to Forex Converter"""
from forex_python.converter import CurrencyRates, CurrencyCodes



currency_codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR','SEK','SGD', 'HKD', 'AUD','CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP' ,'ZAR']


def convert(from_currency, to_currency, amount):
    c = CurrencyRates()
    result = round(c.convert(from_currency, to_currency, int(amount)), 2)
    return result
    


def get_currency_symbol(currency_code):
    curr_codes = CurrencyCodes()
    symbol = curr_codes.get_symbol(currency_code)
    if symbol == None:
        return ""
    else:
        return symbol
    
def invalid_from_code(from_currency):
    if from_currency not in currency_codes:
        return True

def invalid_to_code(to_currency):
    if to_currency not in currency_codes:
        return True

def invalid_amount(amount):
    if amount == "":
        return True