# __getattr__ and __setattr__


class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


empty = Empty()
print(empty.age)  # 40
# print(empty.name)  # AttributeError: name


class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # self.__dict__[attr] = value + 10
            object.__setattr__(self, attr, value)
        else:
            raise AttributeError(attr + ' not allowed')


access = AccessControl()
access.age = 40
print(access.age)  # 50
# access.name = 'Bob'  # AttributeError: name not allowed


# Privacy

class PrivateException(Exception):
    pass


class Privacy:
    def __setattr__(self, attr, value):
        if attr in self.privates:
            raise PrivateException(attr, self)
        else:
            self.__dict__[attr] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


t1 = Test1()
t2 = Test2()
t1.name = 'Bob'
# t2.name = 'Sue'  # PrivateException: ('name', <__main__.Test2 object at 0x0000019781B83BD0>)
print(t1.name)  # Bob
print(t2.name)  # Tom
# t1.age = 30  # PrivateException: ('age', <__main__.Test1 object at 0x000002D697403B50>)
t2.age = 40
print(t2.age)  # 40
