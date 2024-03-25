class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print(f"calls {self.calls} to {self.func.__name__}")
        return self.func(*args)


@Tracer
def spam(a, b, c):
    return a + b + c


print(spam(1, 2, 3))  # calls 1 to spam  6
print(spam('a', 'b', 'c'))  # calls 2 to spam  abc


def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print(f"calls {oncall.calls} to {func.__name__}")
        return func(*args)
    oncall.calls = 0
    return oncall


class C:
    @tracer
    def spam(self, a, b, c):
        return a + b + c


x = C()
print(x.spam(1, 2, 3))  # calls 1 to spam  6
print(x.spam('a', 'b', 'c'))  # calls 2 to spam  abc


def tracer2(func):
    calls = 0

    def oncall(*args):
        nonlocal calls
        calls += 1
        print(f"calls {calls} to {func.__name__}")
        return func(*args)
    return oncall


class C:
    @tracer2
    def spam(self, a, b, c):
        return a + b + c


x = C()
print(x.spam(1, 2, 3))  # calls 1 to spam  6
print(x.spam('a', 'b', 'c'))  # calls 2 to spam  abc