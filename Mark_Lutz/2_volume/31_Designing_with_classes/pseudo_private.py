# Delegation


class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        print('Trace: ' + attr)
        return getattr(self.obj, attr)


x = Wrapper([1, 2, 3])
x.append(4)  # Trace: append
print(x.obj)  # [1, 2, 3, 4]

x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))


# Pseudo-private


class C1:
    def meth1(self):
        self.x = 88

    def meth2(self):
        print(self.x)


class C2:
    def meth1(self):
        self.x = 99

    def meth2(self):
        print(self.x)


class C3(C1, C2):
    pass


c = C3()
c.meth1()
c.meth2()  # 88

# But


class C3(C2, C1):
    pass


c = C3()
c.meth1()
c.meth2()  # 99 already


class C1:
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class C2:
    def meth3(self):
        self.__x = 99

    def meth4(self):
        print(self.__x)


class C3(C2, C1):
    pass


c = C3()
c.meth1(), c.meth3()
c.meth2(), c.meth4()  # 88 99
print(c.__dict__)  # {'_C1__x': 88, '_C2__x': 99}
