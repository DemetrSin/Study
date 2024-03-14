lst = [1, 2]

print(lst)

n = 99


def f():
    global n
    n = 77


print(n)  # 99
f()
print(n)  # 77

z = 100




