# __iter__ and __next__


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1, 5):
    print(i, end=' ')  # 1 4 9 16 25

# But
test = Squares(1, 5)

for i in test:
    for j in test:
        print(i, ':', j, end=' ')  # 1 : 4 1 : 9 1 : 16 1 : 25

# And

for i in Squares(1, 5):
    for j in Squares(1, 5):
        print(i, ':', j, end=' ')  # 1 : 1 1 : 4 1 : 9 1 : 16 1 : 25 4 : 1 4 : 4 4 : 9
        # 4 : 16 4 : 25 9 : 1 9 : 4 9 : 9 9 : 16 9 : 25 16 : 1 16 : 4 16 : 9
        # 16 : 16 16 : 25 25 : 1 25 : 4 25 : 9 25 : 16 25 : 25


# OR With yield

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


for i in Squares(1, 5):
    print(i, end=' ')  #  4 9 16 25

# But this supports the another possibility

test = Squares(1, 5)
print()

for i in test:
    for j in test:
        print(i, ':', j, end=' ')  # 1 : 1 1 : 4 1 : 9 1 : 16 1 : 25 4 : 1 4 : 4 4 : 9
        # 4 : 16 4 : 25 9 : 1 9 : 4 9 : 9 9 : 16 9 : 25 16 : 1 16 : 4 16 : 9
        # 16 : 16 16 : 25 25 : 1 25 : 4 25 : 9 25 : 16 25 : 25


# OR Without yield but with many states

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return SquaresIter(self.start, self.stop)


class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1, 5):
    print(i, end=' ')  #  4 9 16 25
print('\n'*5)

test = Squares(1, 5)

for i in test:
    for j in test:
        print(i, ':', j, end=' ')  # 1 : 1 1 : 4 1 : 9 1 : 16 1 : 25 4 : 1 4 : 4 4 : 9
        # 4 : 16 4 : 25 9 : 1 9 : 4 9 : 9 9 : 16 9 : 25 16 : 1 16 : 4 16 : 9
        # 16 : 16 16 : 25 25 : 1 25 : 4 25 : 9 25 : 16 25 : 25


# Keep going

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

alpha = 'abcdef'
skipper = SkipObject(alpha)
i = iter(skipper)
print(next(i), next(i), next(i))  # a c e
for x in skipper:
    for y in skipper:
        print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee

s = 'abcdef'
for x in s[::2]:
    for y in s[::2]:
        print(x + y, end=' ')  # # aa ac ae ca cc ce ea ec ee

s = 'abcdef'
s = s[::2]
for x in s:
    for y in s:
        print(x + y, end=' ')  # # aa ac ae ca cc ce ea ec ee
print()


# OR Option with yield

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


alpha = 'abcdef'
skipper = SkipObject(alpha)
i = iter(skipper)
print(next(i), next(i), next(i))  # a c e
for x in skipper:
    for y in skipper:
        print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee

s = 'abcdef'
for x in s[::2]:
    for y in s[::2]:
        print(x + y, end=' ')  # # aa ac ae ca cc ce ea ec ee

s = 'abcdef'
s = s[::2]
for x in s:
    for y in s:
        print(x + y, end=' ')  # # aa ac ae ca cc ce ea ec ee
