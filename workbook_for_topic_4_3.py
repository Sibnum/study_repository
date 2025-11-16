from datetime import time


def to_usual_time_format(hour=0, minute=0, meridiem=None):
    error = ''
    if not 0 <= minute <= 59:
        error += str(minute) + ' '
    if not 0 <= hour <= 11:
        error += str(hour) + ' '
    if meridiem != 'am' and meridiem != 'pm':
        error += meridiem + ' '
    if error != '':
        return f'Некорректный ввод: {error}'
    if meridiem == 'am':
        hour_24 = 0 if hour == 12 else hour
    else:
        hour_24 = 12 if hour == 12 else hour + 12
    return time(hour_24, minute, 0)


print(to_usual_time_format(0, 0, 'am'))  # 00:00:00
print(to_usual_time_format(0, 0, 'pm'))  # 12:00:00
print(to_usual_time_format(11, 30, 'pm'))  # 23:30:00
print(to_usual_time_format(5, 45, 'am'))  # 05:45:00
