
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
    
def conversion_result(code):
    getcontext().prec = 2
    now = datetime.now()
    



print(universal_converter('DE')) # Местная дата и время: 21.08.2025 23:24 Uhr, местный курс к рублю: 93.763
print(universal_converter('DE', 100)) # Местная дата и время: 21.08.2025 23:24 Uhr, 100 RUB = 1.07 EUR
print(universal_converter('De', 100)) # Ошибка ввода: code De
print(universal_converter('us', 322)) # Местная дата и время: 21/08/2025 23:24, 322 RUB = 4.06 USD
print(universal_converter('cnn', -1)) # Ошибка ввода: rub_amount -1