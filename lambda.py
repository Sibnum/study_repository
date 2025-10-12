people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(
    lambda item:
    print(f'Здравствуй, {item}!') 
    if item[0] == 'С' 
    else print(f'Привет, {item}!'),
    people)
