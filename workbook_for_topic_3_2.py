def get_envelope(length: int, width: int) -> str:
    if width > length:
        width, length = length, width
    if length <= 15 and width <= 10:
        return 'Подходящий конверт 1'
    elif length <= 25 and width <= 15:
        return 'Подходящий конверт 2'
    elif length <= 34 and width <= 22:
        return 'Подходящий конверт 3'
    else:
        return 'Подходящий конверт не найден'


print(get_envelope(5, 16))
print(get_envelope(30, 15))
print(get_envelope(35, 23))
