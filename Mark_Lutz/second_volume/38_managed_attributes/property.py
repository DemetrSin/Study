class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('fetch ...')
        return self._name

    def set_name(self, value):
        print('change ...')
        self._name = value

    def del_name(self):
        print('remove ...')
        del self._name

    name = property(get_name, set_name, del_name, 'name property docs')


bob = Person('Bob')
print(bob.name)
bob.name = 'Robert'
print(bob.name)
print(Person.name.__doc__)
del bob.name


class PropSquare:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value ** 2

    def set(self, value):
        self.value = value

    x = property(get, set)


square = PropSquare(4)
square2 = PropSquare(10)
print(square2.x)  # 100
print(square.x)  # 16
square.x = 5
print(square.x)  # 25
print(square.value)  # 5


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "name property docs"
        print('fetch ...')
        return self._name

    @name.setter
    def name(self, value):
        print('set ...')
        self._name = value

    @name.deleter
    def name(self):
        print('del ...')
        del self._name


bob = Person('Bob')
print(bob.name)
bob.name = 'Robert'
print(bob.name)
print(Person.name.__doc__)
del bob.name
