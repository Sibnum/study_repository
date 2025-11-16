	# Создайте переменную is_night и запишите в нее True если сейчас ночь, 
    # иначе False

# Если сейчас ночь, то совершите необходимые действия из условия задачи

	# Рассчитайте результат
from decimal import Decimal, getcontext


def currency_converter(convert_time, amount, currency_rate):
    if amount <= 0:
        return 'amount не может быть меньше или равно 0.'
    if currency_rate <= 0:
        return 'currency_rate не может быть меньше или равно 0.'
    getcontext().prec = 3
    amount_dec = Decimal(amount)
    rate_dec = Decimal(currency_rate)
    night_start = '01:00'
    night_end = '08:00'






print(currency_converter("10:00", -5, 1.5))  # amount не может быть меньше или равно 0.
print(currency_converter("10:00", 100, 0))  # currency_rate не может быть меньше или равно 0.
print(currency_converter("03:00", 100, 1)) # 105
print(currency_converter("00:59", 100, 1)) # 100
print(currency_converter("08:00", 100, 1)) # 100
print(currency_converter("14:59", 50000, 3)) # 1.50E+5