import math

print([ord(x) for x in 'spam'])  # [115, 112, 97, 109]
print(list(map(ord, 'spam')))  # [115, 112, 97, 109]
print([x**2 for x in range(10)])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([x for x in range(5) if x % 2 == 0])  # [0, 2, 4]
print(list(filter(lambda x: x % 2 == 0, range(5))))  # [0, 2, 4]
res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
print(res)  # [0, 2, 4]

print([x**2 for x in range(10) if x % 2 == 0])  # [0, 4, 16, 36, 64]
print(list(map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10)))))  # [0, 4, 16, 36, 64]

print([x + y for x in range(3) for y in range(3)])  # [0, 1, 2, 1, 2, 3, 2, 3, 4]
res = []
for x in range(3):
    for y in range(3):
        res.append(x + y)
print(res)  # [0, 1, 2, 1, 2, 3, 2, 3, 4]

print([x + y for x in 'spam' for y in 'SPAM'])
print([x + y for x in 'spam' if x in 'sp' for y in 'SPAM' if y in 'AM'])  # ['sA', 'sM', 'pA', 'pM']
print([x + y + z for x in 'spam' if x in 'sp' for y in 'SPAM' if y in 'AM' for z in '123' if z > '1'])
# ['sA2', 'sA3', 'sM2', 'sM3', 'pA2', 'pA3', 'pM2', 'pM3']  ^^^

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]  ^^^
res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)  # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

print([row[1] for row in m])  # [2, 5, 8]
print([m[row][1] for row in range(3)])  # [2, 5, 8]
print([m[i][i] for i in range(len(m))])  # [1, 5, 9]
print([m[i][len(m) - 1 - i] for i in range(len(m))])  # [3, 5, 7]

l = [[1, 2, 3], [4, 5, 6]]
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] += 10
print(l)  # [[11, 12, 13], [14, 15, 16]]

print([col + 10 for row in m for col in row])  # [11, 12, 13, 14, 15, 16, 17, 18, 19]
res = []
for row in m:
    for col in row:
        res.append(col + 10)
print(res)  # [11, 12, 13, 14, 15, 16, 17, 18, 19]

print([[col + 10 for col in row] for row in m])  # [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
res = []
for row in m:
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)
print(res)  # [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

print([m[row][col] * n[row][col] for row in range(3) for col in range(3)])
# [2, 4, 6, 12, 15, 18, 28, 32, 36]  ^^^
print([[m[row][col] * n[row][col] for col in range(3)] for row in range(3)])
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]  ^^^
res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(m[row][col] * n[row][col])
    res.append(tmp)
print(res)  # [[2, 4, 6], [12, 15, 18], [28, 32, 36]]


print([[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(m, n)])
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]  ^^^
res = []
for (row1, row2) in zip(m, n):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)
print(res)  # [[2, 4, 6], [12, 15, 18], [28, 32, 36]]

print([line.rstrip() for line in open('t.txt')])
print([line.rstrip() for line in open('t.txt').readlines()])
print(list(map(lambda x: x.rstrip(), open('t.txt'))))
# ['aaaa', 'bbbb', 'cccc'] same for every line above

tuples = [('bob', 35, 'male'), ('linda', 40, 'female')]
print([age for (name, age, gender) in tuples])  # [35, 40]
print(list(map(lambda row: row[1], tuples)))  # [35, 40]


# GENERATIONS

def gen_squares(n):
    for i in range(n):
        yield i ** 2


for i in gen_squares(5):
    print(i, end='>')  # 0>1>4>9>16>


def ups(line):
    for sub in line.split(','):
        yield sub.upper()


print(tuple(ups('aaa,bbb,ccc')))  # ('AAA', 'BBB', 'CCC')
print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})  # {0: 'AAA', 1: 'BBB', 2: 'CCC'}


def gen():
    for i in range(10):
        x = yield i
        print(x)


g = gen()
print(next(g))  # 0
print(g.send(77))
print(next(g))
print(g.send(77))


print(x ** 2 for x in range(5))  # <generator object <genexpr> at 0x0000016875A78040>
print((x ** 2 for x in range(5)))  # <generator object <genexpr> at 0x0000016875A78040>
print(list(x ** 2 for x in range(5)))  # [0, 1, 4, 9, 16]

g = (x ** 2 for x in range(5))
print(iter(g) is g)  # True


print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))  # AAABBBCCC
a, b, c = (x.upper() + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a)  # AAA and \n

print(sum(x * 2 for x in range(5)))  # 20
print(sorted(x ** 2 for x in range(5)))  # [0, 1, 4, 9, 16]
print(sorted((x ** 2 for x in range(5)), reverse=True))  # [16, 9, 4, 1, 0]


print(list(map(abs, [-1, -2, -3, 4])))  # [1, 2, 3, 4]
print(list(abs(x) for x in [-1, -2, -3, 4]))  # [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, range(4))))  # [0, 1, 4, 9]
print(list(x ** 2 for x in range(4)))  # [0, 1, 4, 9]

line = 'aaa,bbb,ccc'
print(''.join(x.upper() for x in line.split(',')))  # AAABBBCCC
print(''.join([x.upper() for x in line.split(',')]))  # AAABBBCCC
print(''.join(map(str.upper, line.split(','))))  # AAABBBCCC
print(''.join(map(lambda x: x * 2, line.split(','))))  # aaaaaabbbbbbcccccc
print(''.join(x * 2 for x in line.split(',')))  # aaaaaabbbbbbcccccc

print([x * 2 for x in [abs(x) for x in [-1, -2, 3, -4]]])  # [2, 4, 6, 8]
print(list(map(lambda x: x * 2, map(abs, [-1, -2, 3, -4]))))  # [2, 4, 6, 8]
print(list(x * 2 for x in (abs(x) for x in [-1, -2, 3, -4])))  # [2, 4, 6, 8]

print(list(map(math.sqrt, (x ** 2 for x in range(5)))))  # [0.0, 1.0, 2.0, 3.0, 4.0]


line = 'aa bbb c'
print(''.join(x for x in line.split() if len(x) > 1))  # aabbb
print(''.join(filter(lambda x: len(x) > 1, line.split())))  # aabbb
print(''.join(x.upper() for x in line.split() if len(x) > 1))  # AABBB
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))   # AABBB
res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)  # AABBB


G = (c * 4 for c in 'SPAM')
print(list(G))  # ['SSSS', 'PPPP', 'AAAA', 'MMMM']


def times_four(s):
    for c in s:
        yield c * 4


print(list(times_four('SPAM')))  # ['SSSS', 'PPPP', 'AAAA', 'MMMM']

G = times_four('SPAM')
print(next(G))  # SSSS
print(next(G))  # PPPP
i = iter(G)  # ['AAAA', 'MMMM']
print(list(i))

g = times_four('SPAM')
print(next(g))  # SSSS
print(next(g))  # PPPP


G = (c * 4 for c in 'SPAM')
I = iter(G)
print(next(I))  # SSSS
i = iter(G)
print(next(i))  # PPPP
print(next(I))  # AAAA
print(next(i))  # MMMM


line = 'aa bbb c'


def gensub(s):
    for x in s.split():
        if len(x) > 1:
            yield x.upper()


print(''.join(gensub(line)))  # AABBB
print(gensub(line))  # <generator object gensub at 0x000001CCAA1399A0>
print(gensub(line).__next__())  # AA
print(gensub(line).__next__())  # AA

g = gensub(line)
print(iter(g) is g)  # True
print(id(iter(g)), id(g))  # 1640124684704 1640124684704
# So sure
print(id(iter(g)) == id(g))  # True

print(next(g))  # AA
print(next(g))  # BBB


def both(n):
    for i in range(n):
        yield i
    for i in (x ** 2 for x in range(n)):
        yield i


print(list(both(5)))  # [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]


def both_new(n):
    yield from range(n)
    yield from (x ** 2 for x in range(n))


print(list(both_new(5)))  # [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]
print(': '.join(str(i) for i in both_new(5)))  # 0: 1: 2: 3: 4: 0: 1: 4: 9: 16


def f(a, b, c):
    return f"{a},{b} and {c}"


print(f(*range(3)))  # 0,1 and 2
print(f(*(i for i in range(3))))  # 0,1 and 2
print(f(*[i for i in range(3)]))  # 0,1 and 2

d = {'a': 'Alfa', 'b': 'Beta', 'c': 'Cetta'}

print(f(*d))  # a,b and c
print(f(**d))  # Alfa,Beta and Cetta
print(f(*d.values()))  # Alfa,Beta and Cetta


l, s = [1, 2, 3], 'spam'

for i in range(len(s)):
    s = s[1:] + s[:1]
    print(s, end=' ')  # pams amsp mspa spam

for i in range(len(l)):
    l = l[1:] + l[:1]
    print(l, end=' ')  # [2, 3, 1] [3, 1, 2] [1, 2, 3]

for i in range(len(s)):
    s = s[i:] + s[:i]
    print(s, end=' ')  # spam pams mspa amsp


def scramble(seq):
    res = []
    for i in range(len(seq)):
        seq = seq[i:] + seq[:i]
        res.append(seq)
    return res


print(scramble('spam'))  # ['spam', 'pams', 'mspa', 'amsp']


def scramble2(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


print(scramble2('spam'))  # ['spam', 'pams', 'amsp', 'mspa']

for x in scramble2((1, 2, 3)):
    print(x, end=' ')  # (1, 2, 3) (2, 3, 1) (3, 1, 2)


def scramble_gen(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq


def scramble_gen2(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


print(list(scramble_gen('spam')))  # ['pams', 'amsp', 'mspa', 'spam']
print(list(scramble_gen2((1, 2, 3))))  # [(1, 2, 3), (2, 3, 1), (3, 1, 2)]

for x in scramble_gen2((1, 2, 3)):
    print(x, end=' ')

s = 'spam'
g = (s[i:] + s[:i] for i in range(len(s)))
print(list(g))  # ['spam', 'pams', 'amsp', 'mspa']
t = (1, 2, 3)
g = (t[i:] + t[:i] for i in range(len(t)))
print(list(g))  # [(1, 2, 3), (2, 3, 1), (3, 1, 2)]

f = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(list(f(s)))  # ['spam', 'pams', 'amsp', 'mspa']
print(list(f(t)))  # [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
for x in f(t):
    print(x)


def permute(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute(rest):
                res.append(seq[i:i+1] + x)
        return res


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x


print(permute('abc'))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(list(permute2('abc')))  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print(permute(''))  # ['']
# print(permute((list(range(10)))))
# print(list(permute2((list(range(10))))))


def my_map(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


print(my_map(abs, [-2, -1, 3, -4]))  # [2, 1, 3, 4]
print(my_map(pow, [1, 2, 3], [4, 5, 6, 7]))  # [1, 32, 729]


def my_map2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


print(my_map2(abs, [-2, -1, 3, -4]))  # [2, 1, 3, 4]
print(my_map2(pow, [1, 2, 3], [4, 5, 6, 7]))  # [1, 32, 729]


def map_gen(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


print(list(map_gen(abs, [-2, -1, 3, -4])))  # [2, 1, 3, 4]
print(list(map_gen(pow, [1, 2, 3], [4, 5, 6, 7])))  # [1, 32, 729]


def map_gen2(func, *seqs):
    return (func(*args) for args in zip(*seqs))


print(list(map_gen2(abs, [-2, -1, 3, -4])))  # [2, 1, 3, 4]
print(list(map_gen2(pow, [1, 2, 3], [4, 5, 6, 7])))  # [1, 32, 729]


def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)


print(list(myzip('123', 'abcd')))  # [('1', 'a'), ('2', 'b'), ('3', 'c')]


def myzip2(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]


def my_map_pad(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    index = range(maxlen)
    return [tuple((s[i] if len(s) > i else pad)for s in seqs) for i in index]


s1, s2 = 'abc', 'xyz123'
print(myzip2(s1, s2))  # [('a', 'x'), ('b', 'y'), ('c', 'z')]
print(my_map_pad(s1, s2))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
print(my_map_pad(s1, s2, pad=99))  # [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]

# Scope/ Namespaces

y = 99
for y in 'spam':
    pass

print(y)  # m

y = 'aaa'


def f():
    x = 'bbb'
    return ''.join(z for z in x + y)


# print(z)  # NameError: name 'z' is not defined
# print(x)  # NameError: name 'x' is not defined
print(y)  # aaa
print(f())  # bbbaaa

# Comprehensions

print({x * x for x in range(5)})  # {0, 1, 4, 9, 16}
print(set(x * x for x in range(5)))  # {0, 1, 4, 9, 16}
print({x: x * x for x in range(5)})  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(dict((x, x * x) for x in range(5)))  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(x)  # NameError: name 'x' is not defined

res = set()
for x in range(5):
    res.add(x * x)
print(res)  # {0, 1, 4, 9, 16}
print(x)  # 4 !!!

res = dict()
for x in range(5):
    res[x] = x * x
print(res)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(x)  # 4 !!!!

print({x * x for x in range(10) if x % 2 == 0})  # {0, 64, 4, 36, 16}
print({x: x * x for x in range(10) if x % 2 == 0})  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})  # {5, 6, 7, 8, 9}
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})  # {1: 6, 2: 6, 3: 6}

print({x + y for x in 'ab' for y in 'cd'})  # {'ad', 'ac', 'bc', 'bd'}
print({f'{x}:{y}': (ord(x), ord(y)) for x in 'ab' for y in 'cd'})
# {'a:c': (97, 99), 'a:d': (97, 100), 'b:c': (98, 99), 'b:d': (98, 100)}
print({k * 2 for k in ['spam', 'ham', 'sausages'] if k[0] == 's'})
# {'spamspam', 'sausagessausages'}
print({k.upper(): k * 2 for k in ['spam', 'ham', 'sausages'] if k[0] == 's'})
# {'SPAM': 'spamspam', 'SAUSAGES': 'sausagessausages'}
