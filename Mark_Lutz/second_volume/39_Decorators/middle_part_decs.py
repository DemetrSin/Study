registry = {}


def register(obj):
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    return x ** 2


@register
def ham(x):
    return x ** 2


@register
class Eggs:
    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print('Registry: ')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))
    #  spam => <function spam at 0x000002759C8F9080> <class 'function'>
    # ham => <function ham at 0x000002759C973D80> <class 'function'>
    # Eggs => <class '__main__.Eggs'> <class 'type'>

print('\nManual calls :')
print(spam(2))  # 4
print(ham(2))  # 4
x = Eggs(2)
print(x)  # 16
print('\nRegistry calls')
for name in registry:
    print(name, '=>', registry[name](2))
    # spam => 4
    # ham => 4
    # Eggs => 16

print(registry)  # {'spam': <function spam at 0x0000019A9CC29080>, 'ham': <function ham at 0x0000019A9CCA3D80>, 'Eggs': <class '__main__.Eggs'>}


def decorate(func):
    func.attr = True
    return func


@decorate
def func():
    pass


print(func.attr)  # True


def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate


@annotate('spam data')
def spam(a, b):
    return a + b


print(spam(1, 2), spam.label)  # 3 spam data
