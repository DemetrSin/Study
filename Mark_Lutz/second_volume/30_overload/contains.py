# __contains__

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print(f"get{i}:")
        return self.data[i]

    def __iter__(self):
        print('iter=>', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next=>', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


iters = Iters([1, 2, 3, 4, 5])
print(3 in iters)  # contains: True
for i in iters:
    print(i, end=' | ')  # iter=>next=>1 | next=>2 | next=>3 | next=>4 | next=>5 | next=>
print()
print([i ** 2 for i in iters])  # iter=>next=>next=>next=>next=>next=>next=>[1, 4, 9, 16, 25]
print(list(map(bin, iters)))  # iter=>next=>next=>next=>next=>next=>next=>['0b1', '0b10', '0b11', '0b100', '0b101']
i = iter(iters)  # Manual iteration (what other contexts do)
while True:
    try:
        print(next(i), end=' @ ')  # iter=>next=>1 @ next=>2 @ next=>3 @ next=>4 @ next=>5 @ next=>
    except StopIteration:
        break


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print(f"get{i}:")
        return self.data[i]

    def __iter__(self):
        print('iter=> next:', end='')
        for x in self.data:
            yield x
            print('next:', end='')

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


iters = Iters([1, 2, 3, 4, 5])
print(3 in iters)  # contains: True
for i in iters:
    print(i, end=' | ')  # iter=>next=>1 | next=>2 | next=>3 | next=>4 | next=>5 | next=>
print()
print([i ** 2 for i in iters])  # iter=>next=>next=>next=>next=>next=>next=>[1, 4, 9, 16, 25]
print(list(map(bin, iters)))  # iter=>next=>next=>next=>next=>next=>next=>['0b1', '0b10', '0b11', '0b100', '0b101']
i = iter(iters)  # Manual iteration (what other contexts do)
while True:
    try:
        print(next(i), end=' @ ')  # iter=>next=>1 @ next=>2 @ next=>3 @ next=>4 @ next=>5 @ next=>
    except StopIteration:
        break
