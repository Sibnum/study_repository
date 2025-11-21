
	# Исходя из введенного кода страны вызовите функцию conversion_result() с параметрами соответствующими этому коду
from datetime import datetime
from decimal import Decimal, getcontext


def universal_converter(code, rub_amount=0):
    if rub_amount < 0:
        return f'Ошибка ввода: rub_amount {rub_amount}'
    correct_codes = {'DE', 'US', 'CNN', 'de', 'us', 'cnn'}
    if not code in correct_codes:
        return f'Ошибка ввода: code {code}'
    conversion_result(code)
    if rub_amount == 0:
        return (
            f'Местная дата и время: {now}, '
            f'местный курс к рублю: {conversion_result(code)}'
        )
    elif code == 'DE' or code == 'de':
        now_de = now.strftime("%d.%m.%Y %H:%M")
        return (
            f'Местная дата и время: {now_de} Uhr, '
            f'{rub_amount} RUB = {conversion_result(code)} EUR'
        )
    elif code == 'US' or code == 'us':
        now_us = now.strftime("%d/%m/%Y %H:%M")
        return (
            f'Местная дата и время: {now_us}, '
            f'{rub_amount} RUB = {conversion_result(code)} USD'
        )
    
    
def conversion_result(code):
    
    
    
now = datetime.now()
getcontext().prec = 2

print(universal_converter('DE')) # Местная дата и время: 21.08.2025 23:24 Uhr, местный курс к рублю: 93.763
print(universal_converter('DE', 100)) # Местная дата и время: 21.08.2025 23:24 Uhr, 100 RUB = 1.07 EUR
print(universal_converter('De', 100)) # Ошибка ввода: code De
print(universal_converter('us', 322)) # Местная дата и время: 21/08/2025 23:24, 322 RUB = 4.06 USD
print(universal_converter('cnn', -1)) # Ошибка ввода: rub_amount -1