import one
from one import for_from

one.lst.append(1000)
n = 100

print(n)  # 100
print(one.n)  # 77
print(for_from)  # 1

for_from = 372
print(for_from)  # 372


def i():
    from one import n
    print(n)


i()  # 77

from one import n


def i2():
    print(n)


i2()  # 77
print(n)  # 77

z = 1000

one.change = 1001


def f():
    return f1()


def f1():
    return 'Hello Python'


print(f())  # Hello Python
