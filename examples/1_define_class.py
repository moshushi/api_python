"""
Пример создания классов в Python
"""


class ClassName:
    """
     Тестовый абстрактный класс
    """


class Armor:
    """
    Произвольный другой класс
    """


someobject = ClassName()
someobject1 = ClassName()

# Проверка, что instance (объект) является объектом данного класса
print(isinstance(someobject, ClassName))
print(isinstance(someobject, Armor))
print(8 * "-")


# Наследование

class New(ClassName):
    """
    Тестовый наследуемый класс от ClassName
    """


# Проверка, что класс распространяется на объект наследника
newR = New()
print(isinstance(someobject, New))
print(isinstance(newR, ClassName))
