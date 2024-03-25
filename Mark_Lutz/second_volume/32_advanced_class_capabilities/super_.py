# super

class C:
    def act(self):
        print('spam')


class D(C):
    def act(self):
        super().act()
        print('eggs')


d = D()
d.act()  # spam    eggs


class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()
        # print(self.__class__.__bases__[0])  # <class '__main__.C'>


e = E()
e.method()  # <super: <class 'E'>, <E object>>   spam


class A:
    def act(self):
        print('a')


class B:
    def act(self):
        print('b')


class C(A):
    def act(self):
        super().act()


c = C()
c.act()  # a


class C(A, B):
    def act(self):
        super().act()


c = C()
c.act()  # a


class C(B, A):
    def act(self):
        super().act()


c = C()
c.act()  # b


class C(A, B):
    def act(self):
        A.act(self)
        B.act(self)


c = C()
c.act()  # a   b


class C:
    def __getitem__(self, item):
        print('index C')


class D(C):
    def __getitem__(self, item):
        print('index D')
        C.__getitem__(self, item)
        super().__getitem__(item)
        # super()[item]  # TypeError: 'super' object is not subscriptable


c = C()
c[99]  # index C
d = D()
d[99]  # index D   index C   index C


class A:
    def m(self):
        print('A.m')


class B:
    def m(self):
        print('B.m')


class C(A):
    def m(self):
        super().m()


c = C()
c.m()  # A.m
C.__bases__ = (B,)
c.m()  # B.m
print(C.mro())  # [<class '__main__.C'>, <class '__main__.B'>, <class 'object'>]


# without super

class C(A):
    def m(self):
        C.__bases__[0].m(self)


c = C()
c.m()  # A.m
C.__bases__ = (B,)
c.m()  # B.m


# Multiple inheritance

class A:
    def __init__(self):
        print('A.init')


class B:
    def __init__(self):
        print('B.init')


class C(A, B):
    pass


c = C()  # A.init


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()  # A.init   B.init


class A:
    def __init__(self):
        print('A.init')


class B(A):
    def __init__(self):
        print('B.init')


class C(A):
    def __init__(self):
        print('C.init')
        A.__init__(self)


c = C()  # C.init  A.init
print()
b = B()  # B.init


class D(B, C):
    pass


d = D()  # B.init
print()


class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)


d = D()  # B.init  C.init  A.init
print('\n' * 5)


# with super

class A:
    def __init__(self):
        print('A.init')


class B(A):
    def __init__(self):
        print('B.init')
        super().__init__()


class C(A):
    def __init__(self):
        print('C.init')
        super().__init__()


b = B()  # B.init  A.init
c = C()  # C.init  A.init


class D(B, C):
    pass


d = D()  # B.init  C.init  A.init


# mixing


class A:
    def other(self):
        print('A Other')


class Mixin(A):
    def other(self):
        print('Mixin Other')
        super().other()


class B:
    def method(self):
        print('B Method')


class C(Mixin, B):
    def method(self):
        print('C method')
        super().other()
        super().method()


c = C()
c.method()  # C method  Mixin Other  A Other  B Method
print(C.mro())
# [<class '__main__.C'>, <class '__main__.Mixin'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
