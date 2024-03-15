class C1:
    def __init__(self, who):
        self.name = who

    def set_default(self):
        self.name = 'Default'


class C2(C1):
    def set_default(self):
        self.name = 'Own version'


class C(C1):
    pass


i = C('Demetr')
i1 = C1('Nick')
i2 = C2('Alina')


print(i1)  # <__main__.C object at 0x000001D952542D10>
print(C2)  # <class '__main__.C2'>
print(C)  # <class '__main__.C'>
print(i.name)  # Demetr
print(i1.name)  # Nick
print(i2.name)  # Alina


def defaulter(lst):
    final_data = []
    for x in lst:
        x.set_default()
        final_data.append(x)
    return [x.name for x in final_data]


print(defaulter([i, i1, i2]))  # ['Default', 'Default', 'Own version']


def set_attr(func, attr_name, *args, **kwargs):
    setattr(func, attr_name, *args, **kwargs)


set_attr(defaulter, 'first', [i, i1, i2])


print([x.name for x in defaulter.first])
defaulter.second = defaulter([i2, i, i1])
print(defaulter.__dict__)
# {'first': [<__main__.C object at 0x0000017BD82531D0>, <__main__.C1 object at 0x0000017BD8253090>,
# <__main__.C2 object at 0x0000017BD8253190>], 'second': ['Own version', 'Default', 'Default']}
