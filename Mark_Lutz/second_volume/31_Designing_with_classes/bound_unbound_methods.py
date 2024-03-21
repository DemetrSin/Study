# bound method and unbound method

class Spam:
    def do(self, message):
        print(message)


spam = Spam()
x = spam.do
x('it is x')  # it is x
y = Spam.do
y(spam, 'it is y')  # it is y


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


egg = Eggs()
egg.m2()  # 42


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2


x = Selfless(2)
print(x.normal(3, 4))  # 9
print(Selfless.normal(x, 3, 4))  # 9
print(Selfless.selfless(3, 4))  # 7
# print(x.selfless(3, 4))  # TypeError: Selfless.selfless() takes 2 positional arguments but 3 were given
