# __lt__, __qt__


class C:
    data = 'spam'

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


c = C()
print(c.data < 'ham')  # False
print(c.data > 'ham')  # True


# __bool__ and __len__


class Truth:
    def __bool__(self):
        return True


t = Truth()
if t:
    print('yes')  # yes


class Truth:
    def __bool__(self):
        return False


t = Truth()
print(bool(t))  # False


class Truth:
    def __len__(self):
        return 0


t = Truth()
if not t:
    print('no!')  # no!


class Truth:
    def __bool__(self):
        return True

    def __len__(self):
        return 0


t = Truth()
if t:
    print('yes')  # yes


class Truth:
    pass


t = Truth()
print(bool(t))  # True


# __del__


class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)


brian = Life('Brian')
brian.live()
brian = 'loretta'
"""Output:
Hello Brian
Brian
Goodbye Brian
"""
