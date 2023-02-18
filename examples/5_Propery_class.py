from random import randint

def get_price():
    return randint(50, 200)

class SomeSome():
    def __int__(self, armor, weapon):
        self.armor = armor
        self.weapon = weapon

    @property
    def price(self):
        return get_price()

tank = SomeSome()

print(tank.price)
print(tank.price)
print(tank.price)
print(tank.price)