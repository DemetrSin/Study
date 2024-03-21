import timeit
import time
import math
from functools import reduce


# Exercise 1


def f(x):
    print(x)


# f()  # TypeError: f() missing 1 required positional argument: 'x'
f('spam')  # spa,
f(29)  # 29
f([1, 2, 3])  # [1, 2, 3]
# f(1, 2)  # TypeError: f() takes 1 positional argument but 2 were given


# Exercise 2


def adder(x, y):
    return x + y


adder(20, 25)
adder('sp', 'am')
adder((1, 2), ('spam',))
adder([1, 2], ['spam'])


# Exercise 3


def adder3(*args):
    tot = args[0]
    for x in args[1:]:
        tot += x
    return tot, type(tot)


print(adder3(1, 2, 3, 4, 5))  # (15, <class 'int'>)
print(adder3('sp', 'am', '1'))  # ('spam1', <class 'str'>)
print(adder3([1, 3,], ['aps']))  # ([1, 3, 'aps'], <class 'list'>)
print(adder3((1, 3,), ('aps',)))  # ((1, 3, 'aps'), <class 'tuple'>)


# Exercise 4


def adder4(good=1, bad=2, ugly=3):
    return good + bad + ugly


print(adder4())  # 6
print(adder4(3))  # 8
print(adder4(3, 5))  # 11
print(adder4(3, 5, 6))  # 14
# print(adder4(3, 5, 5, 19))  # TypeError: adder4() takes from 0 to 3 positional arguments but 4 were given


def adder_kwarg(**kwargs):
    tot = None
    for x in kwargs:
        if not tot:
            tot = kwargs[x]
            continue
        tot += kwargs[x]
    return tot


def adder2(**args):                 # Sum any number of keyword args
    argskeys = list(args.keys())    # list needed in 3.X!
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot


print(adder_kwarg(good=4, bad=12, ugly=16))  # 32
print(adder_kwarg(good='s', bad='p', ugly='am'))  # spam
print(adder_kwarg(good=[1, 2], bad=[45, 6], ugly=['am']))  # [1, 2, 45, 6, 'am']
print(adder_kwarg(good=(1, 2), bad=(45, 6), ugly=('am',)))  # (1, 2, 45, 6, 'am')


def timeit_wrapper(func, *args, **kwargs):
    return timeit.timeit(lambda: func(*args, **kwargs), number=100000)


def average_execution_time(func, *args, **kwargs):
    total_time = 0
    num_runs = 10
    for _ in range(num_runs):
        total_time += timeit_wrapper(func, *args, **kwargs)
    return total_time / num_runs


inputs = [
    {'good': 4, 'bad': 12, 'ugly': 16},
    {'good': 's', 'bad': 'p', 'ugly': 'am'},
    {'good': [1, 2], 'bad': [45, 6], 'ugly': ['am']},
    {'good': (1, 2), 'bad': (45, 6), 'ugly': ('am',)},
    {'good': 10, 'bad': 20, 'ugly': 30, 'excellent': 40},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    {'x': [10, 20], 'y': [30, 40], 'z': [50, 60]},
]


dif = 0
for input_data in inputs:
    avg_time_kwarg = average_execution_time(adder_kwarg, **input_data)
    avg_time_adder2 = average_execution_time(adder2, **input_data)
    print("Average execution time for adder_kwarg:", avg_time_kwarg)
    print("Average execution time for adder2:", avg_time_adder2)
    dif += avg_time_kwarg - avg_time_adder2
    print("Difference:", avg_time_kwarg - avg_time_adder2)
    print()

print(dif)


# Exercise 5

test_d = {k: v for k in range(10) for v in 'spam'}
test_d2 = {k: k ** 2 for k in range(10, 20)}


def copy_dict(d):
    return {k: v for k in d for v in d.values()}


print(copy_dict(test_d))


# Exercise 6

def add_dict(d1, d2):
    new = {}
    for key in d1:
        new[key] = d1[key]
    for key in d2:
        new[key] = d2[key]

    return new


print(add_dict(test_d, test_d2))


# Exercise 7

def f1(a, b):
    return a, b


def f2(a, *b):
    return a, b


def f3(a, **b):
    return a, b


def f4(a, *b, **c):
    return a, b, c


def f5(a, b=2, c=3):
    return a, b, c


def f6(a, b=2, *c):
    return a, b, c


print(f1(1, 2))  # (1, 2)
print(f1(b=2, a=1))  # (1, 2)
print(f2(1, 2, 3))  # (1, (2, 3))
print(f3(1, x=2, y=3))  # (1, {'x': 2, 'y': 3})
print(f4(1, 2, 3, x=2, y=3))  # (1, (2, 3), {'x': 2, 'y': 3})
print(f5(1))  # (1, 2, 3)
print(f5(1, 4))  # (1, 4, 3)
print(f6(1))  # (1, 2, ())
print(f6(1, 3, 4))  # (1, 3, (4,))


# Exercise 8


def prime(y):
    if y <= 1:
        return y, 'not prime'
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                return y, 'has factor', x
            x -= 1
        else:
            return y, 'is prime'


print(prime(13))  # (13, 'is prime')
print(prime(13.0))  # (13.0, 'is prime')
print(prime(15))  # (15, 'has factor', 5)
print(prime(15.0))  # (15.0, 'has factor', 5.0)
print(prime(101))  # (101, 'is prime')
print(prime(-1))  # (-1, 'not prime')
print(prime(0))  # (0, 'not prime')


# Exercise 9
from math import sqrt

lst = [2, 4, 9, 16, 25]


for x in range(len(lst)):
    lst[x] = sqrt(lst[x])
print(lst)  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

# OR
lst = [2, 4, 9, 16, 25]
res = lst[:]
for x in range(len(lst)):
    res[x] = sqrt(res[x])
print(lst)  # [2, 4, 9, 16, 25]
print(res)  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

# OR
res = []
for x in lst:
    res.append(sqrt(x))
print(res)  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]

lst = [2, 4, 9, 16, 25]
print(list(map(lambda x: sqrt(x), lst)))  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
print([sqrt(x) for x in lst])  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]
print(list(sqrt(x) for x in lst))  # [1.4142135623730951, 2.0, 3.0, 4.0, 5.0]


# Exercise 10


def custom_timer(runs=1000000):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(runs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += end - start
            avg_time = total_time / runs
            return f"{func.__name__} >> {total_time} >> {avg_time}"
        return wrapper
    return decorator


@custom_timer()
def my_pow(x):
    return pow(x, 0.5)


print(my_pow(200000000000000000000000000000000000000000))
# 4.472135954999579e+20 >>> my_pow >> 0.19528969996827072 >> 1.9528969996827072e-07


@custom_timer()
def use_sqrt(x):
    return sqrt(x)


print(use_sqrt(200000000000000000000000000000000000000000))
# 4.472135954999579e+20 >>> use_sqrt >> 0.17259750131051987 >> 1.7259750131051988e-07


@custom_timer()
def standard_sqrt(x):
    return x ** 0.5


print(standard_sqrt(200000000000000000000000000000000000000000))
# 4.472135954999579e+20 >>> standard_sqrt >> 0.18260599867790006 >> 1.8260599867790006e-07


@custom_timer()
def lst_comp():
    return [x ** 2 for x in range(100)]


@custom_timer()
def dict_comp():
    return {k: k ** 2 for k in range(100)}


print(lst_comp())  # lst_comp >> 2.6080221015872667 >> 2.608022101587267e-06
print(dict_comp())  # dict_comp >> 3.41428259958775 >> 3.41428259958775e-06


# Exercise 11

def count_down(x):
    if x == 0:
        return 'stop'
    else:
        return x, count_down(x-1)


print(count_down(5))  # (5, (4, (3, (2, (1, 'stop')))))


def count_down2(x):
    yield from range(x, 0, -1)


print(list(count_down(5)))  # [5, (4, (3, (2, (1, 'stop'))))]


# Exercise 12

@custom_timer()
def factorial(z):
    n = 1
    for x in range(z, 0, -1):
        n *= x
    return n


@custom_timer()
def factorial_recursion(z):
    if z == 0 or z == 1:
        return 1
    else:
        return z * factorial_recursion(z - 1)


@custom_timer()
def factorial_reduce(z):
    return reduce(lambda x, y: x * y, range(1, z + 1))


@custom_timer()
def math_factorial(z):
    return math.factorial(z)


print(factorial(6))  # factorial >> 0.2686018012500426 >> 2.686018012500426e-07
# print(factorial_recursion(6))
print(factorial_reduce(6))  # factorial_reduce >> 0.3641667003648763 >> 3.641667003648763e-07
print(math_factorial(6))  # math_factorial >> 0.12732160080850008 >> 1.2732160080850008e-07
