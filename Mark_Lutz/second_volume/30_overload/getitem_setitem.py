# __sub__

class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


x = Number(10)
y = x - 12
print(y.data)  # -2


# __getitem__ and __setitem__
class Indexer:
    def __getitem__(self, index):
        return index ** 2


indexer = Indexer()
print(indexer[3])  # 9

print([indexer[i] for i in range(5)])  # [0, 1, 4, 9, 16]


lst = [5, 6, 7, 8, 9]
print(lst[2:4])  # [7, 8]
print(lst[1:])  # [6, 7, 8, 9]
print(lst[:-1])  # [5, 6, 7, 8]
print(lst[::2])  # [5, 7, 9]
print(lst[slice(2, 4)])  # [7, 8]
print(lst[slice(1, None)])  # [6, 7, 8, 9]
print(lst[slice(None, -1)])  # [5, 6, 7, 8]
print(lst[slice(None, None, 2)])  # [5, 7, 9]


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


indexer = Indexer()
print(indexer[0])  # getitem: 0 and 5
print(indexer[2:4])  # getitem: slice(2, 4, None) and [7, 8]
print(indexer[::2])  # getitem: slice(None, None, 2) and [5, 7, 9]


class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing:', index)
        else:
            print('slicing:', index.start, index.stop, index.step)


indexer = Indexer()
indexer[99]  # indexing: 99
indexer[1:99:2]  # slicing: 1 99 2
indexer[1:]  # slicing: 1 None None


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


x = StepperIndex()
x.data = 'spam'
print(x[1])  # p
for i in x:
    print(i, end=' ')  # s p a m

print('p' in x)  # True
print([c for c in x])  # ['s', 'p', 'a', 'm']
print(list(map(str.upper, x)))  # ['S', 'P', 'A', 'M']
a, b, c, d = x
print(a, b, c, d)  # s p a m
