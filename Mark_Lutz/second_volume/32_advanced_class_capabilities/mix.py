class A:
    attr = 5


class B(A):
    pass


class C(A):
    attr = 10


class D(B, C):
    pass


d = D()
print(d.attr)  # 10
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


class Limiter:
    __slots__ = ['name', 'age', 'job']


l = Limiter()
l.age = 40
print(l.age)  # 40
# l.stage = 'age'  # AttributeError: 'Limiter' object has no attribute 'stage'
print(getattr(l, 'age'))  # 40
print(l.__slots__)  # ['name', 'age', 'job']


class E:
    __slots__ = ['c', 'd']


class D:
    __slots__ = ['a', '__dict__']


x = D()
x.a = 1; x.b = 2; x.c = 4
print(x.a, x.b, x.c)  # 1 2 4
x.age = 'anything'
print(x.__dict__)

for attr in list(getattr(x, '__dict__', [])) + getattr(x, '__slots__', []):
    print(attr, '=>', getattr(x, attr))

print(dir(x))


class Properties:
    def __init__(self, value):
        self.value = value

    def get_age(self):
        return self.value

    def set_age(self, age):
        self._age = age

    age = property(get_age, set_age, None, None)


x = Properties(45)
print(x.age)  # 45
x.age = 20
print(x._age)  # 20


class Operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        print(f"set: {name}, {value}")
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value


x = Operators()
print(x.age)  # 40
x.age = 20  # set: age, 20
print(x.age)  # 40
print(x._age)  # 20
x.job = 'dev'  # set: job, dev
print(x.job)  # dev


class AgeDesc:
    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class Descriptors:
    age = AgeDesc()


x = Descriptors()
print(x.age)  # 40
x.age = 42
print(x._age)  # 42


class Spam:
    instances = 0

    def __init__(self):
        Spam.instances += 1
        print('spam instances', Spam.instances)

    def print_instances():
        print(Spam.instances, ' Spam')


c = Spam()  # spam instances 1
print(Spam.instances)  # 1
x = Spam()  # spam instances 2
print(Spam.instances)  # 2
print(c.instances)  # 2
Spam.print_instances()  # 2  Spam
# x.print_instances()  # TypeError: Spam.print_instances() takes 0 positional arguments but 1 was given


class Methods:
    def imeth(self, x):
        print([self, x])

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print([cls, x])

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)


x = Methods()
x.imeth(1)  # [<__main__.Methods object at 0x0000028AADAD4B90>, 1]
Methods.imeth(x, 2)  # [<__main__.Methods object at 0x0000028AADAD4B90>, 1]

x.smeth(2)  # 2
Methods.smeth(2)  # 2

x.cmeth(3)  # [<class '__main__.Methods'>, 3]
Methods.cmeth(3)  # [<class '__main__.Methods'>, 3]


class Methods:
    def imeth(self, x):
        print(self, x)

    @staticmethod
    def smeth(x):
        print(x)

    @classmethod
    def cmeth(cls, x):
        print(cls, x)

    @property
    def name(self):
        print('Bob ' + self.__class__.__name__)


x = Methods()
x.imeth(1)  # <__main__.Methods object at 0x00000217368F9590> 1
x.smeth(2)  # 2
x.cmeth(3)  # <class '__main__.Methods'> 3
x.name  # Bob Methods
