# Объявите функцию buy_sweeties в параметре money
def buy_sweeties(money: int):
    chupa_chups = 5
    gum = 2
    count_chupa_chups = money // chupa_chups
    count_gum = (money - count_chupa_chups * chupa_chups) // gum
    print(
        f'''На {money} руб. Вася может купить:
Чупа чупсов: {count_chupa_chups} шт.
Жевательных резинок: {count_gum} шт.'''
    )


buy_sweeties(13)
buy_sweeties(1)
buy_sweeties(25)
