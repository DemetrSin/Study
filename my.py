# extension of built-in types




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









