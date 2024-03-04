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


a = 0; b = 9
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
