def very_scary(a: int, b: int) -> float:
    result = (a * b + (a - b) ** 2) ** 3 / (b ** 3 * (a ** 2 + b) ** 2)
    return result


print(very_scary(5, 3))

print(very_scary(-1, 3))
