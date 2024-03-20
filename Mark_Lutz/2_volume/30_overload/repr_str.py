# __repr__ and __str__


class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


adder = Adder()
print(adder)  # <__main__.Adder object at 0x000002435EF33D90>


class AddRepr(Adder):
    def __repr__(self):
        return f"AddRepr {self.data}"


add_repr = AddRepr(2)
print(add_repr + 1)  # None
print(add_repr)  # AddRepr 3
print(str(add_repr), repr(add_repr))  # AddRepr 3 AddRepr 3


class AddStr(Adder):
    def __str__(self):
        return f"Value: {self.data}"


add_str = AddStr(3)
print(add_str + 1)  # None
print(add_str)  # Value: 4 ! but not in console !
print(str(add_str), repr(add_str))  # Value: 4 <__main__.AddStr object at 0x0000022C0B228290>


class AddBoth(Adder):
    def __str__(self):
        return f"Str method: {self.data}"

    def __repr__(self):
        return f"Repr method: {self.data}"


add_both = AddBoth(5)
print(add_both)  # Str method: 5
print(str(add_both), repr(add_both))  # Str method: 5 Repr method: 5


class PrinterStr:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        return str(self.data)


objects = [PrinterStr(5), PrinterStr(3)]
print([x for x in objects])
# [<__main__.PrinterStr object at 0x000002DFD0EBCA50>, <__main__.PrinterStr object at 0x000002DFD0EBC8D0>]
print(objects)
# [<__main__.PrinterStr object at 0x0000017DB229CA50>, <__main__.PrinterStr object at 0x0000017DB229C8D0>]

# BUT !
for x in objects:
    print(x, end=' ')  # 5 3


class PrinterRepr:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


objects = [PrinterRepr(5), PrinterRepr(3)]
for x in objects:
    print(x, end=' | ')  # 5 | 3 |
print([x for x in objects])  # [5, 3]
print(objects)  # [5, 3]
