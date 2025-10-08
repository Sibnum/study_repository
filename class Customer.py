class Customer:

    def __init__(self, name: str):
        self.name = name
        self.__discount = 10

    def set_discount(self, __discount: int):
        if self.__discount > 80:
            self.__discount = 80

    def get_price(self, price: int) -> float:
        self.price = round(price - price * (self.__discount / 100), 2)
        return self.price


customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)

customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
