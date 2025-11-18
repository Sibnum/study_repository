from datetime import datetime
from decimal import Decimal, getcontext


def currency_converter(convert_time, amount, currency_rate):
    if amount <= 0:
        return 'amount не может быть меньше или равно 0.'
    if currency_rate <= 0:
        return 'currency_rate не может быть меньше или равно 0.'
    getcontext().prec = 3
    amount_dec = Decimal(amount)
    rate_dec = Decimal(currency_rate)
    night_start = datetime.strptime('01:00', '%H:%M')
    night_end = datetime.strptime('08:00', '%H:%M')
    convert_time = datetime.strptime(convert_time, '%H:%M')
    if night_start <= convert_time < night_end:
        is_night = True
    else:
        is_night = False
    if is_night:
        result = Decimal(amount_dec) * Decimal(rate_dec) * Decimal('1.05')
    else:
        result = Decimal(amount_dec) * Decimal(rate_dec)
    return result


print(currency_converter("10:00", -5, 1.5))
print(currency_converter("10:00", 100, 0))
print(currency_converter("03:00", 100, 1))
print(currency_converter("00:59", 100, 1))
print(currency_converter("08:00", 100, 1))
print(currency_converter("14:59", 50000, 3))
