def cash_counter(withdrawal: int):
    if withdrawal % 100 == 0:
        is_correct_enter = True
    else:
        is_correct_enter = False

    cash_1000 = withdrawal // 1000
    cash_500 = (withdrawal - cash_1000 * 1000) // 500
    cash_100 = (withdrawal - cash_1000 * 1000 - cash_500 * 500) // 100
    print(f'''Купюр номиналом 100: {cash_100}
Купюр номиналом 500: {cash_500}
Купюр номиналом 1000: {cash_1000}''')
    return is_correct_enter


print(cash_counter(1501))
