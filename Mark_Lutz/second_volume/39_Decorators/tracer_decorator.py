def tracer(a_class):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = a_class(*args, **kwargs)

        def __getattr__(self, item):
            print('Trace: ' + item)
            self.fetches += 1
            return getattr(self.wrapped, item)

    return Wrapper


@tracer
class Spam:
    def display(self):
        print('Spam!' *7)


@tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()  # Trace: display
# Spam!Spam!Spam!Spam!Spam!Spam!Spam!

person = Person('Bob', 20, 20)
person.name  # Trace: name
person.hours  # Trace: hours
person.rate  # Trace: rate
person.pay()  # Trace: pay

print(person.fetches)  # 4
print(food.fetches)  # 1


@tracer
class MyList(list):
    pass


x = MyList([])
x.append(2)  # Trace: append

# OR

WrapList = tracer(list)
x = WrapList([1])
x.append(2)  # Trace: append


# WRONG VERSION!

class Tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print('Trace:' + item)
        return getattr(self.wrapped, item)


@Tracer
class Spam:
    def display(self):
        print('spam'*5)


food = Spam()
food.display()  # Trace:display  spamspamspamspamspam


@Tracer
class Person:
    def __init__(self, name):
        self.name = name


bob = Person('bob')
print(bob.name)  # Trace:name  bob
sue = Person('sue')
print(bob.name)  # Trace:name  sue
