class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return Wrapper(self, instance)


class Wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer
    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    @Tracer
    def last_name(self):
        return self.name.split()[-1]


bob = Person('Bob', 1000)
bob.give_raise(10)  # call 1 to give_raise
bob.last_name()  # call 1 to last_name


# OR

class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"call {self.calls} to {self.func.__name__}")
        self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)
        return wrapper


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer
    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    @Tracer
    def last_name(self):
        return self.name.split()[-1]


bob = Person('Bob', 1000)
bob.give_raise(10)  # call 1 to give_raise
bob.last_name()  # call 1 to last_name
