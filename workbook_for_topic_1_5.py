def get_length_from_perimeter(p):
    return p / 4


def get_cube_volume(side):
    return side ** 3


side = int(get_length_from_perimeter(20))

# Вызвать функцию get_cube_volume() передав аргумент side и вывести результат
# в указанном формате
print('Объём куба:', get_cube_volume(side), 'куб. м')
