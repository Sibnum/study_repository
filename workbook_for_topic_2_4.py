def get_pack_number(candies_number, candies_in_pack=15, defect_percent=5) -> int:
    count_pack = candies_number - ((defect_percent / 100) * candies_number)
    result = int(count_pack / candies_in_pack)
    return result


print('Необходимое количество упаковок:', get_pack_number(100))
