class Super:
    def hello(self):
        self.data1 = 'spam'


class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


sub = Sub()
sub_empty = Sub()

print(sub.__dict__)  # {}
print(sub.__class__)  # <class '__main__.Sub'>
print(Sub.__bases__)  # (<class '__main__.Super'>,)
print(Super.__bases__)  # (<class 'object'>,)

print(sub.__dict__)  # {}
sub.hello()
print(sub.__dict__)  # {'data1': 'spam'}
sub.hola()
print(sub.__dict__)  # {'data1': 'spam', 'data2': 'eggs'}

print(Sub.__dict__)
# {'__module__': '__main__', 'hola': <function Sub.hola at 0x000001FDB9BE3D80>, '__doc__': None}
print(Super.__dict__)
# {'__module__': '__main__', 'hello': <function Super.hello at 0x000001D974B19080>,
# '__dict__': <attribute '__dict__' of 'Super' objects>,
# '__weakref__': <attribute '__weakref__' of 'Super' objects>, '__doc__': None}

print(sub_empty.__dict__)  # {}

print(sub.data1, sub.__dict__['data1'])  # spam spam
sub.data3 = 'toast'
print(sub.__dict__)  # {'data1': 'spam', 'data2': 'eggs', 'data3': 'toast'}
sub.__dict__['data3'] = 'ham'
print(sub.data3)  # ham
print(dir(sub))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 'data1', 'data2', 'data3', 'hello', 'hola']
"""
print(dir(Sub))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 'hello', 'hola']
"""
print(Sub.__class__)  # <class 'type'>




