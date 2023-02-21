"""
Проверка наследования между классами
"""

class A:
    VAR = "A"
    def method(self):
        pass

class B:
    VAR = "B"
    def method(self):
        pass

class C(B, A):
    def method(self):
        print(self.VAR)


class D(C):
    pass

d = D()
print(d.method)
print(d.method())
print(D.__mro__)
print(D.mro())
