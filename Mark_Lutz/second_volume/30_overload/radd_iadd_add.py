# __radd__ and __iadd__

class Commuter1:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('add', self.value, other, end='=')
        return self.value + other

    def __radd__(self, other):
        print('radd', self.value, other, end='=')
        return other + self.value


x = Commuter1(77)
y = Commuter1(777)
print(x + 1)  # add 77 1=78
print(13 + y)  # radd 777 13=790
print(x + y)  # add 77 <__main__.Commuter1 object at 0x000001F30B7C18D0>=radd 777 77=854
print('\n'*5)


class Commuter2:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('add', self.value, other, end='=')
        return self.value + other

    def __radd__(self, other):
        print('radd', self.value, other, end='=')
        return self.__add__(other)


x = Commuter2(77)
y = Commuter2(777)
print(x + 1)  # add 77 1=78
print(13 + y)  # radd 777 13=add 777 13=790
print(x + y)  # add 77 <__main__.Commuter2 object at 0x000002214C6A2D90>=radd 777 77=add 777 77=854
print('\n'*5)


class Commuter3:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('add', self.value, other, end='=')
        return self.value + other

    def __radd__(self, other):
        return self + other


x = Commuter3(77)
y = Commuter3(777)
print(x + 1)  # add 77 1=78
print(13 + y)  # add 777 13=790
print(x + y)  # add 77 <__main__.Commuter3 object at 0x000002411EF23110>=add 777 77=854
print('\n'*5)


class Commuter4:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print('add', self.value, other, end='=')
        return self.value + other

    __radd__ = __add__


x = Commuter4(77)
y = Commuter4(777)
print(x + 1)  # add 77 1=78
print(13 + y)  # add 777 13=790
print(x + y)  # add 77 <__main__.Commuter4 object at 0x000002CD55CA3210>=add 777 77=854
print('\n'*5)


class Commuter5:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.value
        return Commuter5(self.value + other)

    def __radd__(self, other):
        return Commuter5(other + self.value)

    def __str__(self):
        return f"Commuter5: {self.value}"


x = Commuter5(100)
y = Commuter5(77)
print(x + 10)  # Commuter5: 110
print(10 + y)  # Commuter5: 87
z = x + y
print(z)  # Commuter5: 177
print(z + 10)  # Commuter5: 187
print(z + z)  # Commuter5: 354
print(z + z + 1)  # Commuter5: 355


# Commuter5 without checking if isinstance


class Commuter6:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Commuter5(self.value + other)

    def __radd__(self, other):
        return Commuter5(other + self.value)

    def __str__(self):
        return f"Commuter5: {self.value}"


x = Commuter6(100)
y = Commuter6(77)
print(x + 10)  # Commuter5: 110
print(10 + y)  # Commuter5: 87
z = x + y
print(z)  # Commuter5: Commuter5: 177
print(z + 10)  # Commuter5: Commuter5: 187
print(z + z)  # Commuter5: Commuter5: Commuter5: Commuter5: 354
print(z + z + 1)  # Commuter5: Commuter5: Commuter5: Commuter5: 355


for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5, Commuter6):
    print('-' * 60)
    x = klass(88)
    y = klass(99)
    print(x + 1)
    print(1 + y)
    print(x + y)

"""Output:
------------------------------------------------------------
add 88 1=89
radd 99 1=100
add 88 <__main__.Commuter1 object at 0x0000016F258F3AD0>=radd 99 88=187
------------------------------------------------------------
add 88 1=89
radd 99 1=add 99 1=100
add 88 <__main__.Commuter2 object at 0x0000016F258F3C90>=radd 99 88=add 99 88=187
------------------------------------------------------------
add 88 1=89
add 99 1=100
add 88 <__main__.Commuter3 object at 0x0000016F258F3A10>=add 99 88=187
------------------------------------------------------------
add 88 1=89
add 99 1=100
add 88 <__main__.Commuter4 object at 0x0000016F258F3AD0>=add 99 88=187
------------------------------------------------------------
Commuter5: 89
Commuter5: 100
Commuter5: 187
------------------------------------------------------------
Commuter5: 89
Commuter5: 100
Commuter5: Commuter5: 187
"""


class Number:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self


x = Number(5)
x += 1
print(x.value)  # 6

y = Number([1])
y += [2]
y += [3]
print(y.value)  # [1, 2, 3]


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other)


x = Number(5)
x += 1
print(x.value)  # 6

y = Number([1])
y += [2]
y += [3]
print(y.value)  # [1, 2, 3]
