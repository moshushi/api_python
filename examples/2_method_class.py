"""
Модуль показывающий, как задавать классам методы
"""


class Animal:
    """
    Абстрактный класс животных
    """
    foot = 4

    def go(self):
        print("I'm going")


crocodile = Animal()

crocodile.go()

print(Animal.foot)
print(crocodile.foot)
