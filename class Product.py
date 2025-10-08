class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_basic_info(self):
        return f'{self.name} (в наличии: {self.quantity})'

    def get_full_info(self):
        pass


class Kettlebell(Product):
    def __init__(self, name, quantity, weight):
        self.weight = weight
        super().__init__(name, quantity)

    def get_full_info(self):
        return f'{self.get_basic_info()}. Вес: {self.weight} кг'

class Clothing(Product):
    def __init__(self, name, quantity, size):
        self.size = size
        super().__init__(name, quantity)

    def get_full_info(self):
        return f'{self.get_basic_info()}. Размер: {self.size}'



small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')


print(small_kettlebell.get_full_info())
print(shirt.get_full_info())
