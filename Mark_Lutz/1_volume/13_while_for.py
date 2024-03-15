import os

c = 0
while True:
    print('Am I an endless cycle?')
    c += 1
    if c:
        print('No.')  # No.
        break

x = 'spam'
while x:
    print(x, end='>')  # spam>pam>am>m>
    x = x[1:]

a = 0;
b = 9
while a < b:
    print(a, end='>')  # 0>1>2>3>4>5>6>7>8>
    a += 1
else:
    print('I\'m else and working always when Python does not meet "break"')  # Works

# while True: pass  # endless and useless
# while True: ...  # same as above

x = ...  # just gag
print(x)  # Ellipsis
print(bool(x))  # True !!!

c = 10
while c:
    c -= 1
    if c % 2 != 0: continue
    print(c, end='>')  # 8>6>4>2>0>

c = 0
while c < 12:
    c += 3
    if c == 9: continue
    if c == 9: break  # Unreachable

while True:
    name = input('Name:')
    if name == 'stop': break
    age = input('Age:')
    print(f"Hello: {name}. Your age is: {age}")

file = open('t.txt', 'r')
while True:
    char = file.read(1)
    if not char: break
    print(char)

while True:
    line = file.readline()
    if not line: break
    print(line.rstrip())

file = open('t.txt', 'rb')
while True:
    chunk = file.read(10)
    if not chunk: break
    print(chunk)

# FOR


t = [(1, 2), (3, 4), (5, 6)]
for a, b in t:
    print(a, b, end='>')  # 1 2>3 4>5 6>
# OR, but first preferable
for pac in t:
    a, b = pac
    print(a, b, end='>')  # 1 2>3 4>5 6>

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c, end='>')  # 1 2 3>4 5 6>

for ((a, b), c) in [([1, 2], 3), ['xy', 6]]:
    print(a, b, c, end='>')  # 1 2 3>x y 6>

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c, end='>')  # 1 [2, 3] 4>5 [6, 7] 8>

tests = [(5, 4), 3.14]
items = ['111', 'aaa', 3.14, (5, 6)]

for key in tests:
    for item in items:
        if key == item:
            print(key, 'was found')  # 3.14 was found
            break
    else:
        print(key, 'wasn\'t found')  # (5, 4) wasn't found

# The same but shorter

for key in tests:
    if key in items:
        print(key, 'was found')  # 3.14 was found
    else:
        print(key, 'wasn\'t found')  # (5, 4) wasn't found

seq1 = 'spam'
seq2 = 'scam'
res = []

for x in seq1:
    if x in seq2:
        res.append(x)

print(x)  # m - This is the last step in cycle
print(res)  # ['s', 'a', 'm']
print([x for x in seq1 if x in seq2])  # ['s', 'a', 'm'] Same as cycle above

for char in open('t.txt', 'r').read():
    print(char)

for line in open('t.txt').readlines():
    print(line.rstrip())

for line in open('t.txt'):  # Same as above
    print(line.rstrip())

s = 'spam'
for i in range(4):
    s = s[1:] + s[:1]
    print(s, end=' ')  # pams amsp mspa spam

for i in range(len(s)):
    s = s[i:] + s[:i]
    print(s, end=' ')  # spam pams mspa amsp

l = [1, 2, 3, 4, 5]

for i in l:
    i += 1
print(l)  # [1, 2, 3, 4, 5] Not good

for i in range(len(l)):
    l[i] += 1
print(l)  # [2, 3, 4, 5, 6] Nice

i = 0
while i < len(l):
    l[i] += 1
    i += 1
print(l)  # [3, 4, 5, 6, 7] But for cycle more preferable

print([x + 1 for x in l])  # Good way but not changes the exactly l

s = 'spam'
for (offset, item) in enumerate(s):
    print(f"{item} appears at offset {offset}")

enum_s = enumerate(s)
print(next(enum_s))  # (0, 's')
print(next(enum_s))  # (1, 'p')
for offset, item in enum_s:  # same as cycle above but harder to read
    print(f"{item} appears at offset {offset}")

print([c * i for i, c in enumerate(s)])  # ['', 'p', 'aa', 'mmm']

for i, l in enumerate(open('t.txt'), start=1):
    print(f"{i} >>> {l}")

print(os.system('systeminfo'))
for line in os.popen('systeminfo'):
    print(line.rstrip())

for line in os.popen('systeminfo'):
    parts = line.split(':')
    if parts and parts[0].lower() == 'system type':
        print(parts[1].strip())

# Zip

l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]
print(list(zip(l1, l2)))  # [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
for x, y in zip(l1, sorted(l2, reverse=True)):
    print(x, y, '--', x + y)

t1, t2, t3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(t1, t2, t3)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

s1 = 'seq'
s2 = 'abc123'

print(list(zip(s1, s2)))  # [('s', 'a'), ('e', 'b'), ('q', 'c')]

keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {}
for k, v in zip(keys, values):
    d[k] = v
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# OR

keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3} Bingo!)

# OR!
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3} Yep!)
