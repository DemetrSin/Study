import copy
d = {1: '1', 2: '2', 'l': [3, 4, 5], 'd': {1: '1', 2: '2'}}
# dc = copy.deepcopy(d)

b = d.copy()
b['d'][1] = 'one'
# b[1] = 'one'
# dc['d'][1] = 'one'

print(d)
# print(b)
# print(dc)


