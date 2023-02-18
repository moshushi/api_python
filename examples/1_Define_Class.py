"""
Пример создания классов в Python
"""


class ClassName:
    pass


class Armor:
    pass


someobject = ClassName()
someobject1 = ClassName()

# Проверка, что инстанс(объект) является объектом данного класса
print(isinstance(someobject, ClassName))
print(isinstance(someobject, Armor))
print(8*"-")

# Наследование

class New(ClassName):
    pass


# Проверка, что класс расспространяется на объект наследника
newR = New()
print(isinstance(someobject, New))
print(isinstance(newR, ClassName))
