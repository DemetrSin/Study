import one

one.lst.append(1000)
n = 100

print(n)  # 100
print(one.n)  # 77


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
