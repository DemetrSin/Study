def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'


x = C(6, 7)
print(x.attr)


# wrong example

class Decorator:
    def __init__(self, C):
        self.C = C

    def __call__(self, *args):
        self.wrapped = self.C(*args)
        return self

    def __getattr__(self, item):
        return getattr(self.wrapped, item)


@Decorator
class C:
    def __init__(self, x):
        self.attr = 'spam'


x = C(5)
y = C(5)
print(x.attr)
print(y.attr)


def d1(f):
    return lambda: 'x' + f()


def d2(f):
    return lambda: 'y' + f()


def d3(f):
    return lambda: 'z' + f()


@d1
@d2
@d3
def func():
    return 'spam'


print(func())  # xyzspam
