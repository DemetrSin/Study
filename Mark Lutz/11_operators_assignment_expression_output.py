from copy import deepcopy
import sys

t = (1, 2, 3)
a, b, c = t
print(a, b, c, type(a))  # 1 2 3 <class 'int'>
a, *b = t
print(f"{a}, > {b}, > {type(b)}")  # 1, > [2, 3], > <class 'list'>
a, b, *c = 'spam'
print(f"{a}, {b}, {c}")  # s, p, ['a', 'm']
spam = ham = 'me'
print(f"{id(spam)}\n {id(ham)}\n {spam} == {ham}")  # equal
s = 'spam'
a, b, c = list(s[:2]) + [s[2:]]
print(a, b, c, sep=',')  # s,p,am
a = s[:3]
print(a)  # spa
(a, b), c = s[:2], s[2:]
print(a, b, c, sep=',')  # s,p,am
a, b, c = range(3)
print(a, b, c)  # 0 1 2


l = [0, 1, 2, 3]
while l:
    front, l = l[0], l[1:]
    print(front, l)
"""
Output:
    0 [1, 2, 3]
    1 [2, 3]
    2 [3]
    3 []
"""

l = [0, 1, 2, 3]
while l:
    front, *l = l
    print(front, l)  # same result as above

s = 'spam'
*a, b, c = s
print(a, b, c)  # ['s', 'p'] a m
a, *b, c = s
print(a, b, c)  # s ['p', 'a'] m
a, *b, c, d, e = s
print(a, b, c, d, e)  # s [] p a m
a, b, c, d, *e = s
print(a, b, c, d, e)  # s p a m []
*a, b, c, d, e = s
print(a, b, c, d, e)  # [] s p a m
*a, b, c, d = s
print(a, b, c, d)  # ['s'] p a m
# *a = s  # SyntaxError: starred assignment target must be in a list or tuple
*a, = s  # Works
print(a)  # ['s', 'p', 'a', 'm']

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)  # 1 [2, 3] 4 \n 5 [6, 7] 8


a = b = 0
b += 1
print(a, b)  # 0 1
a = b = [0]
b[0] = 45
print(a, b, sep='>>>')  # [45]>>>[45]

a = []
b = a.copy()
b.append(45)
print(a, b)  # [] [45]
a = [[]]
b = a.copy()
b[0].append(45)
print(a, b)  # !!!! It is> [[45]] [[45]], but
a = [[]]
b = deepcopy(a)  # !!!!
b[0].append(45)
print(a, b)  # Nice> [[]] [[45]]
# OR
a, b = [], []
a.append(1)
b.append(45)
print(a, b)  # [1] [45]


l = [1, 2]
m = l
l = l + [3, 4]  # concatenation always creates new object!
print(l, m)  # [1, 2, 3, 4] [1, 2]
l = [1, 2]
m = l
l += [3, 4]  # it works like method "extend"
print(l, m)  # [1, 2, 3, 4] [1, 2, 3, 4]

f = open('t.txt', 'w')
print(l, m, file=f)  # Adds data to file
f.close()


sys.stdout.write('hello world\n')  # hello world
temp = sys.stdout
sys.stdout = open('t.txt', 'a')  # we can use print as logs
print('Try it')  # writes to file
sys.stdout.close()
sys.stdout = temp
sys.stdout = sys.__stdout__  # works as line above
print('Back here')  # Back here
print(open('t.txt').read())


