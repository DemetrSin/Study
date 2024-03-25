# Exercise 1


class Adder:
    def add(self, x, y):
        print('Not Implemented')


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        d = {}
        for k, v in x.items():
            d[k] = v
        for k, v in y.items():
            d[k] = v
        return d


test1 = {'a': 1, 'b': 2}
test2 = {'c': 3, 'd': 4}

adder = Adder()
adder.add(1, 2)  # Not Implemented

lst_adder = ListAdder()
data = lst_adder.add(list(test1.items()), list(test2.items()))
print(data)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

d_adder = DictAdder()
data = d_adder.add(test1, test2)
print(data)

# Part 2


class Adder:

    def __init__(self, obj):
        self.obj = obj

    def __add__(self, other):
        return self.add(self.obj, other.obj)

    def add(self, x, y):
        print('Not Implemented')


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        d = {}
        for k, v in x.items():
            d[k] = v
        for k, v in y.items():
            d[k] = v
        return d


l1 = ListAdder(list(test1.items()))
l2 = ListAdder(list(test2.items()))
print(l1 + l2)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

d1 = DictAdder(test1)
d2 = DictAdder(test2)
print(d1 + d2)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# OR


class Adder:

    def __init__(self, obj):
        self.obj = obj


class ListAdder(Adder):
    def __add__(self, other):
        return self.obj + other


class DictAdder(Adder):
    def __add__(self, other):
        d = self.obj.copy()
        d.update(other)
        return d


l1 = ListAdder(list(test1.items()))
print()
print(l1 + list(test2.items()))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

d1 = DictAdder(test1)
print(d1 + test2)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
