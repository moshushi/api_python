"""
Модуль демонстрирует вычисляемое свойство - property
"""
from random import randint


def get_price():
    """
    Функция генерирует случайную цену из диапазона
    :return: int
    """
    return randint(50, 200)


class SomeWeapon:
    """
    Класс создающий абстрактное оружие
    """

    def __int__(self, armor, weapon):
        self.armor = armor
        self.weapon = weapon

    @property
    def price(self):
        """
        Вывести цену
        :return:
        """
        return get_price()


tank = SomeWeapon()

print(tank.price)
print(tank.price)
print(tank.price)
print(tank.price)
