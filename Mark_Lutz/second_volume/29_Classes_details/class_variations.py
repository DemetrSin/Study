class MixedNames:
    data = 'spam'
    one = 1

    def __init__(self, data):
        self.data = data

    def display(self):
        print(self.data, MixedNames.data)


m = MixedNames('data')
mn = MixedNames('data for mn')

m.display()  # data spam
m.one = 23
print(m.one, mn.one, MixedNames.one)  # 23 1 1
MixedNames.one = 2
print(m.one, mn.one, MixedNames.one)  # 23 2 2

m.data = MixedNames.data
m.display()  # spam spam


class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    def action(self):
        assert False, 'action must be defined'


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('In Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print(f"\n{klass.__name__} ...")
        klass().method()
    print('\nProvider...')
    provider = Provider()
    provider.delegate()

    supers = Super()
    try:
        supers.delegate()  # AssertionError: action must be defined
    except AssertionError:
        pass


