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
