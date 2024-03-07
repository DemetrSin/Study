def f(a):
    a = 99
    return a


b = 77
print(f(b))  # 99


def changer(a, b):
    a = 12
    b[0] = 'spam'


x = 0
lst = [1, 2, 3]  # changer() will touch it
changer(x, lst)
print(x, lst)  # 0 ['spam', 2, 3]


def multiple(x, y):
    x = 10
    y = [1, 3]
    return x, y


x = 1
y = [10, 20]

print(multiple(x, y))  # (10, [1, 3])


def f_args(*args):
    return args


print(f_args(1, 2, [3, 4]))  # (1, 2, [3, 4])
print(f_args(*{1: 2, 4: 4}))  # (1, 4)


def some(**kwargs):
    return kwargs


print(some(name='ivan', age=5))  # {'name': 'ivan', 'age': 5}


def foo(a, b, c):
    return a, b, c


print(foo(*[1, '4', {'some': 142}]))  # (1, '4', {'some': 142})
print(foo(**{'a': 1, 'b': 2, 'c': 3}))  # (1, 2, 3)


def tracer(func, *args, **kwargs):
    print('calling:', func.__name__)
    return func(*args, **kwargs)


def func(a, b, c, d):
    return a + b + c + d


print(tracer(func, *[1, 2], **{'c': 3, 'd': 4}))


# keyword only args


def kwonly(a, *b, c):
    return a, b, c


try:
    print(kwonly(1, 2, 3))  # TypeError: kwonly() missing 1 required keyword-only argument: 'c'
except TypeError:
    pass

print(kwonly(1, 2, c=3))  # (1, (2,), 3)


def kwonly2(a, *, b, c):
    return a, b, c


try:
    print(kwonly2(1, 2, 3))  # TypeError: kwonly2() takes 1 positional argument but 3 were given
except TypeError:
    pass

print(kwonly2(1, b=2, c=3))  # (1, 2, 3)


def min1(*args):
    res = args[0]
    for x in args[1:]:
        if x < res:
            res = x
    return res


def min2(first, *args):
    for x in args:
        if x < first:
            first = x
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min1(*[4, 5, 1, 3, 2]))  # 1
print(min2(*['vsd', 'fdss', 'aa']))  # aa
print(min3([25, 18], [42, 9], [101, 10]))  # [25, 18]


def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res


def less_than(x, y):
    return x < y


def greater_then(x, y):
    return x > y


print(minmax(less_than, 8, 4, 2, 1, 19))  # 1
print(minmax(greater_then, 8, 4, 2, 1, 19))  # 19




