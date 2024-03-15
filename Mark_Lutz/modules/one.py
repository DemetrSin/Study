lst = [1, 2]

print(lst)

n = 99
change = 100
for_from = 1


def f():
    global n
    n = 77


print(n)  # 99
f()
print(n)  # 77

z = 100


if __name__ == '__main__':
    print('I\'m the one.py module')




