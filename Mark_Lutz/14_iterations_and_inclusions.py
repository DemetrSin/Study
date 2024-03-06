import os
from collections.abc import Iterator, Iterable


l = [1, 2, 3]
s = 'spa'
print(isinstance(l, Iterator), isinstance(s, Iterator))  # False False
print(isinstance(l, Iterable), isinstance(s, Iterable))  # True True
i = l.__iter__()
si = iter(s)
print(isinstance(i, Iterator), isinstance(si, Iterator))  # True True
print(isinstance(i, Iterable), isinstance(si, Iterable))  # True True
print(i)  # <list_iterator object at 0x000001673E769870>
print(si)  # <str_ascii_iterator object at 0x000001673E4F9360>
print(i.__next__())  # 1
print(i.__next__())  # 2
print(i.__next__())  # 3
# print(i.__next__())  # StopIteration Error
print(next(si))  # s
print(next(si))  # p
print(next(si))  # a
# print(next(si))  # StopIteration Error

f = open('new.py')
print(f is iter(f))  # True
print(f is f.__iter__())  # True
print(isinstance(f, Iterable), isinstance(f, Iterator))  # True True

p = os.popen('dir')
d = {}  # Already iterator
print(hasattr(p, '__next__'))  # True

e = enumerate('spam')  # Already iterator
print(hasattr(e, '__next__'))  # True
print(e.__next__())  # (0, 's')
print(list(e))  # [(1, 'p'), (2, 'a'), (3, 'm')] cause of previous line without 0, 's'


f = open('new.py')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
print(lines)

# OR
print([line.rstrip() for line in open('new.py').readlines()])  # same output as above

print([(n, line.rstrip()) for n, line in enumerate(open('new.py').readlines()) if line[0] == '#'])


print([x + y for x in 'abc' for y in 'xyz'])  # ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']


print(list(map(lambda x: x.upper(), open('new.py'))))
print(list(map(lambda x: x ** 3, [x for x in range(5)])))  # [0, 1, 8, 27, 64]
print(list(sorted(open('new.py'))))
print(list(zip(open('new.py'), open('new.py'))))
print(list(enumerate([line.strip() for line in open('new.py').readlines()])))
print(list(filter(bool, [line.strip() for line in open('new.py').readlines()])))

print(list(open('new.py')))
print(tuple(open('new.py')))
print('&&'.join(open('new.py')))

a, *b = open('new.py')
print('import' in open('new.py').read())

l = [1, 2, 3, 4]
l[1:3] = open('new.py')
print(l)

l = [45]
l.extend(open('new.py'))
print(l)

l = [45]
l.append(open('new.py'))
print(l)  # [45, <_io.TextIOWrapper name='new.py' mode='r' encoding='cp1251'>]
print(list(l[1]))

print(set(open('new.py')))
print({line.rstrip() for line in open('new.py')})
print({i: line for i, line in enumerate(open('new.py'))})
print({line for line in open('new.py') if line.startswith('#')})
print({i: line for i, line in enumerate(open('new.py')) if line[0] == '#'})
print(len(max(open('new.py'))))
print(len(min(open('new.py'))))


def f(a, b, c, d):
    return ''.join(f"{a}, {b}, {c}, {d}")


print(f(*[1, 2, 3, 4]))
print(f(*[x for x in open('new.py').readline(4)]))


r = range(2)
it1 = iter(r)  #
print(next(it1))  # 0
print(next(it1))  # 1
# print(next(it1))  # StopIteration Error
it2 = iter(r)
print(next(it2))  # 0
print(next(it2))  # 1
# print(next(it2))  # StopIteration Error


m = map(abs, [-1, -2])  # already iterator
print(m.__next__())  # 1
print(m.__next__())  # 2
print([x for x in m])  # []
m = map(abs, [-1, -2])
print([x for x in m])  # [1, 2]
it_m = iter(m)  # Do not create new iterator!!!
# print(next(it_m))  # StopIteration Error


z = zip([1, 2, 3], ['a', 'b', 'c'])  # already iterator
print(list(z))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print([x for x in z])  # []
z = zip([1, 2, 3], ['a', 'b', 'c'])
print([x for x in z])  # [(1, 'a'), (2, 'b'), (3, 'c')]

print(list(filter(bool, ['', 0, 1, 'a'])))  # [1, 'a']
print([x for x in ['', 0, 1, 'a'] if bool(x)])  # [1, 'a']
print([x for x in ['', 0, 1, 'a'] if x])  # [1, 'a'] same as ^, but preferable

d = {1: 'a', 2: 'b', 3: 'c'}
d_keys = d.keys()
# print(next(d))  # TypeError: 'dict' object is not an iterator
d_it = iter(d_keys)
print(next(d_it))  # 1
print(next(d_it))  # 2
print(next(d_it))  # 3
# print(next(d_it))  # StopIteration
d_it2 = iter(d_keys)
print(next(d_it2))  # 1
print(next(d_it2))  # 2

# But we can just make dict as iterator

d_in_it = iter(d)
print(next(d_in_it))  # 1
print(next(d_in_it))  # 2

d_val = d.values()
# print(next(d_val))  # TypeError: 'dict_values' object is not an iterator
d_val_it = d_val.__iter__()
print(d_val_it.__next__())  # a
print(d_val_it.__next__())  # b and etc...

# And we can make it list

print(list(d))  # [1, 2, 3]
print(list(d.keys()))  # [1, 2, 3]
print(list(d.values()))  # ['a', 'b', 'c']
print(list(d.items()))  # [(1, 'a'), (2, 'b'), (3, 'c')]
