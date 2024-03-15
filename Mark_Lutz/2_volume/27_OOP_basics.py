class FirstClass:
    def set_data(self, data):
        self.data = data

    def display(self, attr):
        # for x in self.__dict__:
        #     if x == attr:
        #         return self.__dict__[x]

        # OR

        # return str([self.__dict__[x] for x in self.__dict__ if x == attr][0])

        # OR easiest way

        return self.__dict__[attr]


fa = FirstClass()
fa.set_data('Some data here')
fa.anything = 125
print(fa.display('anything'))  # 125
print(fa.display('data'))  # Some data here


class SecondCLass(FirstClass):
    def display(self, attr):
        return f"Here some data: {self.__dict__[attr]}"


sa = SecondCLass()
sa.set_data('smth')
print(sa.display('data'))  # Here some data: smth


class MyClass:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number}"


one = MyClass(20)
two = MyClass(10)

print(one, two)  # 20 10
print(one.number + two.number)  # 30


class ThirdClass(SecondCLass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f"ThirdClass : {self.data}"

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
print(a.display('data'))  # Here some data: abc
print(a)  # ThirdClass : abc
b = a + 'xyz'
print(b)  # ThirdClass : abcxyz
print(b.display('data'))  # Here some data: abcxyz
a.mul(3)
print(a)  # ThirdClass : abcabcabc



