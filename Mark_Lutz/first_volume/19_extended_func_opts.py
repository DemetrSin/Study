# Recursion
import sys
from functools import reduce


def my_sum(lst):
    if not lst:
        return 0
    return lst[0] + my_sum(lst[1:])


print(my_sum([1, 2, 3, 4, 5]))  # 15
print(my_sum([]))  # 0
# print(my_sum('spam'))  # TypeError: can only concatenate str (not "int") to str


def my_sum2(lst):
    return 0 if not lst else lst[0] + my_sum2(lst[1:])


print(my_sum2([1, 2, 3, 4, 5]))  # 15
print(my_sum2([]))  # 0
# print(my_sum2(['s', 'p', 'a']))  # TypeError
# print(my_sum2('spam'))  # TypeError: can only concatenate str (not "int") to str


def my_sum3(lst):
    return lst[0] if len(lst) == 1 else lst[0] + my_sum3(lst[1:])


print(my_sum3([1, 2, 3, 4, 5]))  # 15
# print(my_sum3([]))  # IndexError
print(my_sum3(['s', 'p', 'a']))  # spa
print(my_sum3('spam'))  # spam


def my_sum4(lst):
    first, *rest = lst
    return first if not rest else first + my_sum4(rest)


print(my_sum4([1, 2, 3, 4, 5]))  # 15
# print(my_sum4([]))  # ValueError
print(my_sum4(['s', 'p', 'a']))  # spa
print(my_sum4('spam'))  # spam


# Indirect recursion

def my_sum_indirect(lst):
    if not lst:
        return 0
    return nonempty(lst)


def nonempty(lst):
    return lst[0] + my_sum_indirect(lst[1:])


print(my_sum_indirect([1.1, 2.2, 3.3, 4.4]))  # 11.0


# Recursion for tree of sublist sum

def sumtree(lst):
    tot = 0
    for x in lst:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


print(sumtree([1, [2, [3, 4], 5], 6, [7, 8]]))  # 36
print(sumtree([1, [2, [3, [4], [5]]]]))  # 15
print(sumtree([[[[[1], 2], 3], 4], 5]))  # 15


def sumtree_while(lst):
    tot = 0
    items = list(lst)
    while items:
        front = items.pop()
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


print(sumtree_while([1, [2, [3, 4], 5], 6, [7, 8]]))  # 36
print(sumtree_while([1, [2, [3, [4], [5]]]]))  # 15
print(sumtree_while([[[[[1], 2], 3], 4], 5]))  # 15


# !!! THIS CODE FROM LUTZ GITHUB !!!

trace = lambda x: None               # or print
visit = lambda x: print(x, end=', ')


def sumtree(L):
    tot = 0
    levels = [L]
    while levels:
        trace(levels)
        front = levels.pop(0)                    # Fetch/delete front path
        for x in front:
            if not isinstance(x, list):
                tot += x                         # Add numbers directly
                visit(x)
            else:
                levels.append(x)                 # Push/schedule nested lists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)
print('-'*40)

# !!! END !!!


def echo(message):
    return message


def foo(func, arg):
    return func(arg)


x = echo
print(x('Python'))
print(foo(echo, 'Some arg'))  # Some arg
t = ((echo, 'Message'), (echo, 'Yet'))
print([func(arg) for func, arg in t])  # ['Message', 'Yet']
for (func, arg) in t:
    print(func(arg))


def make(label):
    def echo2(message):
        return label + ':' + message
    return echo2


f = make('Spam')
print(f('Ham'))  # Spam:Ham


f.count = 0
f.count += 1
f.string = 'Spam'
print(f.count, f.string)  # 1 Spam
print([x for x in dir(f) if not x.startswith('__')])  # ['count', 'string']


def f(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


print(f(1, 2, 3))  # 6
print(f.__annotations__)  # {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}


# lambda


l = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4
]

print([f(2) for f in l])  # [4, 8, 16]
print(l[2](30))  # 810000


def foo():
    title = 'Sir'
    action = lambda x: f"{title} {x}"
    return action


act = foo()
print(act('Demetr'))  # Sir Demetr


d = {
    'one': lambda x: x * 2,
    'two': lambda: 3 * 3,
    'three': lambda: 4 * 4
}

print(d['one'](3))  # 6
print(d['two']())  # 9


show_all = lambda x: list(map(sys.stdout.write, x))
print(show_all(['spam ', 'toast ', 'eggs ']))

showall = lambda x: [sys.stdout.write(line) for line in x]
print(showall(['spam ', 'toast ', 'eggs ']))


def action(x):
    return lambda y: x + y


act = action(99)
print(act(2))  # 101

action = lambda x: lambda y: x + y
act = action(99)
print(act(2))  # 101
print((lambda x: lambda y: x + y)(75)(2))  # 77
print((lambda x: lambda y: lambda z: x + y + z)(75)(2)(700))  # 777

print(list(map(lambda x: x + 3, [1, 2, 3, 4])))  # [4, 5, 6, 7]

pow(3, 4)
print(list(map(pow, [1, 2, 3], [2, 3, 4])))  # [1, 8, 81]

print(list(filter(lambda x: x > 0, range(-5, 5))))  # [1, 2, 3, 4]

print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 24


def my_reduce(function, sequence, default=None):
    if not sequence:
        return default
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally


print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 10
print(my_reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 24
print(my_reduce(lambda x, y: x ** y, []))  # None
print(my_reduce(lambda x, y: x ** y, [], default='Abra'))  # Abra
