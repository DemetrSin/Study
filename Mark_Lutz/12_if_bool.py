d = {'spam': 2.00, 'ham': 3.99, 'egg': 0.15}
print(d.get('spam', 'Bad choice'))  # 2.0
print(d.get('asparagus', 'Bad choice'))  # Bad choice
# OR

choice = 'ham'
if choice in d:
    print(d[choice])  # 3.99
else:
    print('Bad Choice')

# OR
another_choice = 'asparagus'
try:
    print(d[another_choice])
except:
    print('Bad choice')  # Bad choice


print(1 or 3)  # 1
print([] or 3)  # 3
print([] or {})  # {}

print(2 and 3, 3 and 2)  # 3 2
print([] and {})  # []
print(3 and [])  # []

a, b, c = 0, 0, 1
x = a or b or c or None
print(x)  # 1

l = [1, 0, 2, '', False, 'soup', 0, [], 21]
print(list(filter(bool, l)))  # [1, 2, 'soup', 21]
print([x for x in l if x])  # [1, 2, 'soup', 21]
print(any(l), all(l), all([x for x in l if x]))  # True False True
