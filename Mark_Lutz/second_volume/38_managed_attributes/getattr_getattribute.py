class MyTry:
    def __getattr__(self, item):
        if item not in self.__dict__:
            setattr(self, item, None)
        return getattr(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


x = MyTry()
print(x.name)  # None
print(x.x)  # None
x.x = 99
print(x.x)  # 99


class Catcher:
    def __getattr__(self, item):
        print(f"get : {item}")

    def __setattr__(self, key, value):
        print(f"set : {key}, {value}")


x = Catcher()
x.job  # get : job
x.pay  # get : pay
x.pay = 99  # set : pay, 99


class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        print(f'Trace : {item}')
        return getattr(self.obj, item)


x = Wrapper([1, 2, 3])
x.append(4)  # Trace : append
print(x.obj)  # [1, 2, 3, 4]


class Person:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        if attr == 'name':
            print('get')
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print('set')
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print('del')
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]


x = Person('Bob')  # set
x.name  # get
x.name = 'Roberto'  # set
del x.name  # del


class Person:
    def __init__(self, name):
        self._name = name

    def __getattribute__(self, attr):
        print('get ' + attr)
        if attr == 'name':
            attr = '_name'
        return object.__getattribute__(self, attr)


x = Person('Sue')
x.name  # get name


class AttrSquare:
    def __init__(self, value):
        self.value = value

    def __getattr__(self, attr):
        if attr == 'x':
            return self.value ** 2
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'x':
            attr = 'value'
        self.__dict__[attr] = value


a = AttrSquare(3)
b = AttrSquare(32)
print(a.x)  # 9
a.x = 4
print(a.x)  # 16
print(b.x)  # 1024
a.y = 4
print(a.y)  # 4


class AttrSquare:
    def __init__(self, value):
        self.value = value

    def __getattribute__(self, attr):
        if attr == 'x':
            return object.__getattribute__(self, 'value') ** 2
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr == 'x':
            attr = 'value'
        object.__setattr__(self, attr, value)


a = AttrSquare(3)
b = AttrSquare(32)
print(a.x)  # 9
a.x = 4
print(a.x)  # 16
print(b.x)  # 1024
a.y = 4
print(a.y)  # 4


class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        print('getattr: ', attr)
        if attr == 'attr3':
            return 3
        else:
            raise AttributeError(attr)


x = GetAttr()
print(x.attr1)  # 1
print(x.attr2)  # 2
print(x.attr3)  # getattr:  attr3  3


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('getattribute : ', attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


x = GetAttribute()
print(x.attr1)  # getattribute :  attr1  1
print(x.attr2)  # getattribute :  attr2  2
print(x.attr3)  # getattribute :  attr3  3
