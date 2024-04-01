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
print(x.attr)  # spam


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
print(x.attr)  # spam
print(y.attr)  # spam


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


class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        self.func(*args)


@Tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)  # call 1 to spam  6
spam('a', 'b', 'c')  # call 2 to spam abc
print(spam.calls)  # 2
print(spam)  # <__main__.Tracer object at 0x0000019A07D93610>


# the same without decorators

calls = 0


def tracer(func, *args):
    global calls
    calls += 1
    print(f"call {calls} to {func.__name__}")
    func(*args)


def spam(a, b, c):
    print(a + b + c)


tracer(spam, 1, 2, 3)  # call 1 to spam  6
tracer(spam, 'a', 'b', 'c')  # call 2 to spam abc
print(calls)  # 2
print(spam)  # <function spam at 0x000001F856856340>


# with kwargs

class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        self.func(*args, **kwargs)


@Tracer
def spam(a, b, c):
    print(a + b + c)


@Tracer
def eggs(x, y):
    print(x ** y)


spam(a=4, b=5, c=6)   # call 1 to spam  15
eggs(2, 16)  # call 1 to eggs  65536
eggs(4, y=4)  # call 2 to eggs  256


# func option


def tracer(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


print('\n'*5)
spam(a=4, b=5, c=6)   # call 1 to spam  15
eggs(2, 16)  # call 1 to eggs  65536
eggs(4, y=4)  # call 2 to eggs  256


# or with func attrs

def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"call {wrapper.calls} to {func.__name__}")
        func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


print('\n'*5)
spam(a=4, b=5, c=6)   # call 1 to spam  15
eggs(2, 16)  # call 1 to eggs  65536
eggs(4, y=4)  # call 2 to eggs  256
