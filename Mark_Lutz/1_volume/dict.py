print({x: ord(x) for x in 'spam'})

a = {'a': 1, 'c': 3, 'b': 2}
for key in sorted(a):
    print(key, a[key])

# CHAPTER 8

d = {1: 'one', 2: 'two', 3: 'three', 'list': [1, 2, 3]}
print([x for x in d.keys() if isinstance(x, int)])  # [1, 2, 3]
d2 = {'1': 'one', '2': 'two', 3: 3}
d.update(d2)
print(d)  # {1: 'one', 2: 'two', 3: 3, 'list': [1, 2, 3], '1': 'one', '2': 'two'}
print(d2.pop(3))  # 3
print(d2)  # {'1': 'one', '2': 'two'}

print([(value, key) for (key, value) in d.items()])  # Indexing in reverse direction

n = 'two'
print([k for (k, v) in d.items() if v == n])  # [2, '2']
print([k for k in d.keys() if d[k] == n])  # same as above

d_zip = {k: v for k, v in zip([1, 2, 3], ['1', '2', '3'])}
print(d_zip)  # {1: '1', 2: '2', 3: '3'}
d_fromkeys = dict.fromkeys('spam')  # same {k: None for k in 'spam'}
print(d_fromkeys)  # {'s': None, 'p': None, 'a': None, 'm': None}
d_fromkeys = dict.fromkeys([1, 2, 3], 0)  # same {k: 0 for k in range(1, 4)}
print(d_fromkeys)  # {1: 0, 2: 0, 3: 0}

print(d.keys() & d_fromkeys)  # {1, 2, 3} <<< SET!
print(d_fromkeys.items() | d_fromkeys.keys())  # {1, 2, 3, (2, 0), (3, 0), (1, 0)}

unsorted_d = {4: 'four', 1: 'one', 3: 'three'}
""" THE SAME This one
for k in sorted(unsorted_d):
    print(k, unsorted_d[k])

    And this one

sorted_d = list(unsorted_d)
sorted_d.sort()
for k in sorted_d:
    print(k, unsorted_d[k])

Output :
        1 one
        3 three
        4 four
"""
# print([(k, unsorted_d[k]) for k in sorted_d])  # [(1, 'one'), (3, 'three'), (4, 'four')]


di = {1: '1', 2: '2'}
a, b = di.items()
print(a, b)  # (1, '1') (2, '2')