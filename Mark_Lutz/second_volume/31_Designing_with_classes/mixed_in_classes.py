# Mixed-in classes
import importlib


class ListInstance:
    def __attr_names(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f"\t{attr}={self.__dict__[attr]}\n"
        return result

    def __str__(self):
        return f"Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attr_names()}"


class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'


x = Spam()
print(x)  # Instance of Spam, address 2883014959504: data=food


class Super:
    def __init__(self):
        self.data = 'spam'

    def ham(self):
        pass


class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass


x = Sub()
print(x)  # Instance of Sub, address 2687461175376:
# 	data=spam
# 	data2=eggs
# 	data3=42


def tester(lister_class, sept=False):
    class Super:
        def __init__(self):
            self.data = 'spam'

        def ham(self):
            pass

    class Sub(Super, ListInstance):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


def test_by_names(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)


test_by_names('my', 'ListInstance', True)


# Keep Going

class ListInherited:
    def __attr_name(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr [-2:] == '__':
                result += f"\t{attr}\n"
            else:
                result += f"\t{attr}={getattr(self, attr)}\n"
        return result

    def __str__(self):
        return f"Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attr_names()}"
