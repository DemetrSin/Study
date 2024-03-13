import timeit


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


