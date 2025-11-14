def get_triangle_info(a, b, c) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return 'Ошибка ввода!'
    elif a + b < c or a + c < b or b + c < a:
        return 'Треугольник невозможен'
    elif a == b == c:
        return f'Треугольник равносторонний {a * 3}'
    elif a == b != c:
        return f'Треугольник равнобедренный {c}'
    elif b == c != a:
        return f'Треугольник равнобедренный {a}'
    elif a == c != b:
        return f'Треугольник равнобедренный {b}'
    elif a != b != c:
        return f'Треугольник разносторонний {(a + b + c) / 3}'


print(get_triangle_info(2, 2.5, 3)) # Треугольник разносторонний 2.5
print(get_triangle_info(2, 2, 3)) # Треугольник равнобедренный 3
print(get_triangle_info(2, 2, 2)) # Треугольник равносторонний 6
print(get_triangle_info(1, 1, 3)) # Треугольник невозможен
print(get_triangle_info(-1,-2,-3)) # Ошибка ввода!
