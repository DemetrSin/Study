# singleton

instances = {}


def singleton(a_class):
    def on_call(*args, **kwargs):
        if a_class not in instances:
            instances[a_class] = a_class(*args, **kwargs)
        return instances[a_class]
    return on_call


@singleton
class Person:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def pay(self):
        return self.rate * 2


@singleton
class Spam:
    def __init__(self, val):
        self.val = val


bob = Person('bob', 20)
print(bob.name, bob.pay())  # bob 40

sue = Person('sue', 10)
print(sue.name, sue.pay())  # bob 40

x = Spam(val=42)
y = Spam(99)

print(x.val, y.val)  # 42 42
print(instances)  # {<class '__main__.Person'>: <__main__.Person object at 0x0000020F1E393150>,
# <class '__main__.Spam'>: <__main__.Spam object at 0x0000020F1E392F90>}


# or

def singleton(a_class):
    instance = None

    def on_call(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = a_class(*args, **kwargs)
        return instance
    return on_call


@singleton
class Person:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def pay(self):
        return self.rate * 2


@singleton
class Spam:
    def __init__(self, val):
        self.val = val


bob = Person('bob', 20)
print(bob.name, bob.pay())  # bob 40

sue = Person('sue', 10)
print(sue.name, sue.pay())  # bob 40

x = Spam(val=42)
y = Spam(99)

print(x.val, y.val)  # 42 42
print()


# or

def singleton(a_class):
    def on_call(*args, **kwargs):
        if on_call.instance is None:
            on_call.instance = a_class(*args, **kwargs)
        return on_call.instance
    on_call.instance = None
    return on_call


@singleton
class Person:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def pay(self):
        return self.rate * 2


@singleton
class Spam:
    def __init__(self, val):
        self.val = val


bob = Person('bob', 20)
print(bob.name, bob.pay())  # bob 40

sue = Person('sue', 10)
print(sue.name, sue.pay())  # bob 40

x = Spam(val=42)
y = Spam(99)

print(x.val, y.val)  # 42 42
print()


class Singleton:
    def __init__(self, a_class):
        self.a_class = a_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.a_class(*args, **kwargs)
        return self.instance


@Singleton
class Person:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def pay(self):
        return self.rate * 2


@Singleton
class Spam:
    def __init__(self, val):
        self.val = val


bob = Person('bob', 20)
print(bob.name, bob.pay())  # bob 40

sue = Person('sue', 10)
print(sue.name, sue.pay())  # bob 40

x = Spam(val=42)
y = Spam(99)

print(x.val, y.val)  # 42 42
