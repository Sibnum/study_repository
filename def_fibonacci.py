def fibonacci(n : int):
    first_element = 0
    second_element = 1
    for _ in range(n):
        yield first_element
        first_element, second_element = second_element, first_element + second_element


sequence = fibonacci(6)
for number in sequence:
    print(number)
