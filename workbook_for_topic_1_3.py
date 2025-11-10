def count_calories(banana_number=0, apple_number=0, orange_number=0):
    banana_calories = 105 * banana_number
    apple_calories = 52 * apple_number
    orange_calories = 62 * orange_number
    total_calories = banana_calories + apple_calories + orange_calories
    return print(f'Общая калорийность: {total_calories} ккал')


count_calories(banana_number=2, apple_number=3, orange_number=1)

count_calories(apple_number=5, orange_number=3)
