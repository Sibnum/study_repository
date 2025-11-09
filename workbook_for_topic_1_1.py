bananas_in_fridge = 12
apples_in_fridge = 14
oranges_in_fridge = 8

total_fruits_in_fridge = (
    bananas_in_fridge + apples_in_fridge + oranges_in_fridge
)

bananas_in_basket = 2
apples_in_basket = 3
oranges_in_basket = 1

total_fruits_in_basket = (
    bananas_in_basket + apples_in_basket + oranges_in_basket
)

result = total_fruits_in_fridge - (3 * total_fruits_in_basket)

print(f'Фруктов в холодильнике осталось: {result}')
