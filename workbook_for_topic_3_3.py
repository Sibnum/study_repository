def count_discount(goods_number: int, total_price: int) -> str:
    if goods_number <= 0 or total_price <= 0:
        return 'Ошибка ввода!'
    discount = 0
    if goods_number == 1:
        discount = 10
    elif 2 <= goods_number <= 4:
        discount = 15
    elif goods_number >= 5:
        discount = 25
    result_price = round(total_price * (1 - discount / 100), 1)
    sum_of_discount = round(total_price - result_price, 1)
    return (
        f'Сумма общей скидки: {sum_of_discount},'
        f' а итоговая стоимость: {result_price}'
        )


print(count_discount(1, 100))
print(count_discount(5, 322))
print(count_discount(2, 42))
