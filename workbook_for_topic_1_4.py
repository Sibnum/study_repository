def count_flowerbed_perimeter(r: int) -> float:
    pi = 3.14
    result = 2 * pi * r
    return result


print(
    'Для ограждения клумбы необходимо', count_flowerbed_perimeter(1),
    'м бордюра.'
)
