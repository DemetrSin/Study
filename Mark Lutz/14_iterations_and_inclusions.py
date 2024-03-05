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

