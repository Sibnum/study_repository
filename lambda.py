people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda item: print(f'Привет, {item}!'), people)
# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
say_to_all(lambda item: print(f'До завтра, {item}!'), people)