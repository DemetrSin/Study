class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner)


class Subject:
    attr = Descriptor()


s = Subject()
s.attr
Subject.attr


class D:
    def __get__(*args):
        print('get')


class C:
    a = D()


c = C()
c.a  # get
C.a  # get
c.a = 99
print(c.a)  # 99
C.a  # get


class D:
    def __get__(*args):
        print('get')

    def __set__(*args):
        raise AttributeError('cannot set')


class C:
    a = D()


c = C()
c.a  # get
# c.a = 99  # AttributeError: cannot set


class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance._name = value

    def __delete__(self, instance):
        del instance._name


class Super:
    def __init__(self, name):
        self._name = name

    name = Name()


class Person(Super):
    pass


bob = Person('Bob')
print(bob.name)  # Bob
bob.name = 'Roberto'
print(bob.name)  # Roberto
del bob.name
# print(bob.name)  # AttributeError: 'Person' object has no attribute '_name'. Did you mean: 'name'?

# Nested


class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        def __get__(self, instance, owner):
            return instance._name

        def __set__(self, instance, value):
            instance._name = value

        def __delete__(self, instance):
            del instance._name

    name = Name()


bob = Person('Bob')
print(bob.name)  # Bob
bob.name = 'Roberto'
print(bob.name)  # Roberto
print(Person.Name.__doc__)
del bob.name


class DescSquare:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    x = DescSquare(2)


class Client2:
    x = DescSquare(5)


c1 = Client1()
c2 = Client2
print(c1.x)  # 4
c1.x = 4
print(c1.x)  # 16
print(c2.x)  # 25


class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value * 10

    def __set__(self, instance, value):
        self.value = value


class CalcAttrs:
    x = DescState(5)
    y = 4

    def __init__(self):
        self.z = 3


obj = CalcAttrs()
print(obj.x, obj.y, obj.z)  # 50 4 3
obj.x = 10
CalcAttrs.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)  # 100 6 7

obj2 = CalcAttrs()
print(obj2.x, obj2.y, obj2.z)  # 100 6 3
print('\n' * 5)


# Version with instances attribute


class InstState:
    def __get__(self, instance, owner):
        return instance._x * 10

    def __set__(self, instance, value):
        instance._x = value


class CalcAttrs:
    x = InstState()
    y = 4

    def __init__(self):
        self._x = 2
        self.z = 3


obj = CalcAttrs()
print(obj.x, obj.y, obj.z)  # 20 4 3
obj.x = 10
CalcAttrs.y = 6
obj.z = 7
print(obj.x, obj.y, obj.z)  # 100 6 7

obj2 = CalcAttrs()
print(obj2.x, obj2.y, obj2.z)  # 20 6 3


# And Both Options

class DescBoth:
    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        print(self.data, instance.data)

    def __set__(self, instance, value):
        instance.data = value


class Client:
    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')


c = Client('eggs')
c.managed  # spam eggs
c.managed = 'SPAM'
c.managed  # spam SPAM
print(c.__dict__)  # {'data': 'SPAM'}
print([x for x in dir(c) if not x.startswith('__')])  # ['data', 'managed']
print(getattr(c, 'data'))  # SPAM
getattr(c, 'managed')  # spam SPAM
c.s = 's'
print(getattr(c, 's'))  # s
