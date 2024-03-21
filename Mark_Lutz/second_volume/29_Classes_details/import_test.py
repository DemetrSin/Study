import namespaces

y = 1000
print(y)  # 1000
print(namespaces.y)  # 99
namespaces.f()  # 99
namespaces.g()  # 22
print(namespaces.C.y)  # 78

i = namespaces.C()
print(i.y)  # 78
i.m()
print(i.y)  # 64
