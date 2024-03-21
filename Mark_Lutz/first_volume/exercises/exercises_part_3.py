# Exercise one
# a)
s = 'spam'
for x in s:
    print(ord(x))

# OR
print([ord(x) for x in s])  # [115, 112, 97, 109]

# b)
n = 0
for x in s:
    n += ord(x)
print(n)  # 433

# OR
print(sum([ord(x) for x in s]))  # 433

# c)

l = []
for x in s:
    l.append(ord(x))
print(l)  # [115, 112, 97, 109]

# OR

print(list(map(ord, s)))  # [115, 112, 97, 109]

# OR as I did before

print([ord(x) for x in s])  # [115, 112, 97, 109]


# Exercise two

for x in range(50):
    print('hello %d\n\a' % x)  # Probably deprecated syntax
    print(f"hello {x}\n\a")  # Hope this is equivalent for line above


# Exercise three

unsorted_dict = {'d': 2, 'b': 3, 'a': 4, 'c': 1}
print(dict([(k, unsorted_dict[k]) for k in sorted(unsorted_dict)]))  # {'a': 4, 'b': 3, 'c': 1, 'd': 2}

# But I wanna more, than only keys, so keep going

sorted_keys = [k for k in sorted(unsorted_dict)]
sorted_values = [v for v in sorted(unsorted_dict.values())]
print(dict(zip(sorted_keys, sorted_values)))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# OR

print(dict(zip(
    [k for k in sorted(unsorted_dict)],
    [v for v in sorted(unsorted_dict.values())]
    )
    )
)  # shorter, but harder to read. Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Exercise 4

# a)

l = [1, 2, 4, 8, 16, 32, 64]
x = 5
i = 0
while i < len(l):
    if 2 ** x == l[i]:
        print('at index', i)
        break
    i += 1
else:
    print(x, 'not found')


# b)

l = [1, 2, 4, 8, 16, 32, 64]
x = 5
for i in l:
    if 2 ** x == i:
        print('at index', l.index(i))
        break
else:
    print(x, 'not found')


# c)

l = [1, 2, 4, 8, 16, 32, 64]
x = 5
if 2 ** x in l:
    print('at index', l.index(i))
else:
    print(x, 'not found')


# d)


l = []
x = 5
for x in range(7):
    l.append(2 ** x)
if 2 ** x in l:
    print('at index', l.index(2 ** x))
else:
    print(x, 'not found')

# OR

x = 5
l = list(map(lambda x: 2 ** x, range(7)))
if 2 ** x in l:
    print('at index', l.index(2 ** x))
else:
    print(x, 'not found')
