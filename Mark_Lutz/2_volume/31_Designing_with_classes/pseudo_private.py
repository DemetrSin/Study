# Delegation


class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        print('Trace: ' + attr)
        return getattr(self.obj, attr)


x = Wrapper([1, 2, 3])
x.append(4)  # Trace: append
print(x.obj)  # [1, 2, 3, 4]

x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))


# Pseudo-private


class C1:
    def meth1(self):
        self.x = 88

    def meth2(self):
        print(self.x)


class C2:
    def meth1(self):
        self.x = 99

    def meth2(self):
        print(self.x)


class C3(C1, C2):
    pass


c = C3()
c.meth1()
c.meth2()  # 88

# But


class C3(C2, C1):
    pass


c = C3()
c.meth1()
c.meth2()  # 99 already


class C1:
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class C2:
    def meth3(self):
        self.__x = 99

    def meth4(self):
        print(self.__x)


class C3(C2, C1):
    pass


c = C3()
c.meth1(), c.meth3()
c.meth2(), c.meth4()  # 88 99
print(c.__dict__)  # {'_C1__x': 88, '_C2__x': 99}


class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3


x = Number(3)
y = Number(4)
z = Number(5)

print(x.double())  # 6
acts = [x.double, y.triple, z.double]
for act in acts:
    print(act(), end=' ')  # 6 12 10

bound = x.double
print(bound.__self__, bound.__func__)
# <__main__.Number object at 0x000002C35D3F2190> <function Number.double at 0x000002C35D173D80>

lam = lambda x: x ** x
print(lam(3))  # 27


def square(arg):
    return arg ** 2


class Sum:
    def __init__(self, val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]
for act in actions:
    print(act(5), end=' ')  # 25 7 15

print(actions[-1](5))  # 15
print(list(map(lambda act: act(5), actions)))  # [25, 7, 15]
print([x(5) for x in actions])  # [25, 7, 15]
gen = (x(5) for x in actions)
print(gen.__next__())  # 25
print(gen.__next__())  # 7
print(gen.__next__())  # 15
# print(gen.__next__())  # StopIteration


def gen_func():
    for x in actions:
        yield x(5)


print(list(gen_func()))  # [25, 7, 15]
gen2 = gen_func()
print(gen2.__next__())  # 25
print(gen2.__next__())  # 7
print(gen2.__next__())  # 15
# print(gen.__next__())  # StopIteration


class Negate:
    def __init__(self, val):
        self.val = -val

    def __repr__(self):
        return str(self.val)


actions = [square, sobject, lam, pobject.method, Negate]
for act in actions:
    print(act(5), end=' ')  # 25 7 3125 15 -5

d = {act(5): act for act in actions}

for k, v in d.items():
    print(f"{k} => {v}")
"""Output:
25 => <function square at 0x000002D7F14751C0>
7 => <__main__.Sum object at 0x000002D7F14733D0>
3125 => <function <lambda> at 0x000002D7F0FA04A0>
15 => <bound method Product.method of <__main__.Product object at 0x000002D7F1473410>>
-5 => <class '__main__.Negate'>
"""
