# MY Version of playing with
x = 99


def f(x):
    return x


def g(x):
    x = 22
    return x


class C:
    x = 78

    def m(self):
        x = 64
        self.x = x

    def glo(self):
        global x
        self.x = 101
        return x


if __name__ == '__main__':
    c = C()
    print(f(g(C.m(c))))  # 22
    print(g(f(C.m(c))))  # 22
    print(f(C.m(c)))  # None
    print(c.glo())  # 99

# End of version

# Lutz Version

y = 99


def f():
    print(y)


def g():
    y = 22
    print(y)


class C:
    y = 78

    def m(self):
        y = 64
        self.y = y


if __name__ == '__main__':
    print(y)  # 99
    f()  # 99
    g()  # 22
    print(y)  # 99
    obj = C()
    print(obj.y)  # 78
    obj.m()
    print(obj.y)  # 64
    print(C.y)  # 78


# Another Lutz Tricks

z = 11


def g1():
    print(z)


def g2():
    global z
    z = 22


def h1():
    z = 33

    def nested():
        print(z)
    return nested


def h2():
    z = 33

    def nested():
        nonlocal z
        z = 44
        print(z)
    return nested()


if __name__ == '__main__':
    print(z)  # 11
    g1()  # 11
    g2()
    g1()  # 22
    h1_1 = h1()
    h1_1()  # 33
    h2()  # 44


# One Yet Trick

n = 1


def nester():
    print(n)  # 1

    class Class:
        print(n)  # 1

        def method1(self):
            print(n)  # 1

        def method2(self):
            n = 3
            print(n)  # 3

    c = Class()
    c.method1()
    c.method2()


if __name__ == '__main__':
    print(n)
    nester()
    print('-'*40)
    """Output: 
    1
    1
    1
    1
    3
    """


# Second Trick

n = 1


def nester():
    n = 2
    print(n)  # 2

    class Class:
        print(n)  # 2

        def method1(self):
            print(n)  # 2

        def method2(self):
            n = 3
            print(n)  # 3

    c = Class()
    c.method1()
    c.method2()


if __name__ == '__main__':
    print(n)
    nester()
    print('-'*40)
    """Output: 
    1
    2
    2
    2
    3
    """


# Third Trick

n = 1


def nester():
    n = 2
    print(n)  # 2

    class Class:
        n = 3
        print(n)  # 3

        def method1(self):
            print(n)  # 2
            print(self.n)  # 3

        def method2(self):
            n = 4
            print(n)  # 4
            self.n = 5
            print(self.n)  # 5

    c = Class()
    c.method1()
    c.method2()


if __name__ == '__main__':
    print(n)
    nester()
    print('-'*40)
    """Output: 
    1
    2
    3
    2
    3
    4
    5
    """
