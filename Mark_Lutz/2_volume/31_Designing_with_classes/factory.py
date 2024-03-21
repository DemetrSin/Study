# Factory

def factory(Class, *args, **kwargs):
    return Class(*args, **kwargs)


class Spam:
    def do_it(self, message='default'):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

    def info(self):
        print(self.name, self.job, self.__class__.__name__)


object1 = factory(Spam)
object2 = factory(Person, 'Arthur', 'King')
object3 = factory(Person, name='Brian')

object1.do_it(99)  # 99


lst = [object1, object2, object3]
for x in lst:
    method = getattr(x, [y for y in dir(x) if not y.startswith('_')][0])
    method()
"""Output:
default
Arthur King Person
Brian None Person
"""
