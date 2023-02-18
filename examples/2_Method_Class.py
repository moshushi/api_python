class Animal():
    foot = 4

    def go(self):
        print("I'm going")

crokodile = Animal()

# print(crokodile.go())
crokodile.go()

print(Animal.foot)
print(crokodile.foot)