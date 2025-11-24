# нужно переделать под словарь, иначе тренажёр не пропустит

from datetime import datetime
from decimal import Decimal, getcontext


def universal_converter(code, rub_amount=0):
    if rub_amount < 0:
        return f'Ошибка ввода: rub_amount {rub_amount}'
    correct_codes = {'DE', 'US', 'CNN', 'de', 'us', 'cnn'}
    if code not in correct_codes:
        return f'Ошибка ввода: code {code}'
    now = datetime.now()
    if code == 'DE' or code == 'de':
        dt_format = now.strftime("%d.%m.%Y %H:%M Uhr")
        currency_rate = 93.763
        currency_symbol = 'EUR'
    elif code == 'US' or code == 'us':
        dt_format = now.strftime("%d/%m/%Y %H:%M")
        currency_rate = 79.322
        currency_symbol = 'USD'
    elif code == 'CNN' or code == 'cnn':
        dt_format = now.strftime("%d-%m-%Y %H:%M")
        currency_rate = 11.164
        currency_symbol = 'CNY'
    if rub_amount == 0:
        now = now.strftime("%d.%m.%Y %H:%M")
        return (
            f'Местная дата и время: {dt_format}, '
            f'местный курс к рублю: {currency_rate}'
        )
    else:
        result = conversion_result(
            dt_format, currency_rate, currency_symbol, rub_amount
        )
        return result


def conversion_result(dt_format, currency_rate, currency_symbol, rub_amount=0):
    getcontext().prec = 3
    if currency_symbol == 'EUR':
        result_dec = Decimal(str(rub_amount)) / Decimal(str(currency_rate))
        return (
            f'Местная дата и время: {dt_format}, '
            f'{rub_amount} RUB = {result_dec} {currency_symbol}'
        )
    elif currency_symbol == 'USD':
        result_dec = Decimal(str(rub_amount)) / Decimal(str(currency_rate))
        return (
            f'Местная дата и время: {dt_format}, '
            f'{rub_amount} RUB = {result_dec} {currency_symbol}'
        )
    elif currency_symbol == 'CNY':
        result_dec = Decimal(str(rub_amount)) / Decimal(str(currency_rate))
        return (
            f'Местная дата и время: {dt_format}, '
            f'{rub_amount} RUB = {result_dec} {currency_symbol}'
        )


print(universal_converter('DE'))  # Местная дата и время: 21.08.2025 23:24 Uhr, местный курс к рублю: 93.763
print(universal_converter('DE', 100))  # Местная дата и время: 21.08.2025 23:24 Uhr, 100 RUB = 1.07 EUR
print(universal_converter('De', 100))  # Ошибка ввода: code De
print(universal_converter('us', 322))  # Местная дата и время: 21/08/2025 23:24, 322 RUB = 4.06 USD
print(universal_converter('cnn', -1))  # Ошибка ввода: rub_amount -1
