import sys
from Mark_Lutz import docstrings


print(len([x for x in dir(sys) if not x.startswith('_')]))  # 72
print([x for x in dir([]) if x[0] != '_'])  # First option, but they are all the same
print([x for x in dir([]) if not x[0] == '_'])  # Second
print([x for x in dir([]) if not x.startswith('_')])  # Third


def dir1(name):
    return [x for x in dir(name) if not x.startswith('__')]


print(dir1(tuple))  # ['count', 'index']

print(dir1(str) == dir1(''))  # True
print(dir(int) == dir(45))  # True
print(dir(tuple) == dir(([], {}, set())))  # True


print(docstrings.docs_func.__doc__)  # Some func docs
print(docstrings.__doc__)  # Some module docs
print(docstrings.DocsClass.__doc__)  # Some class docs
print(docstrings.DocsClass.docs_method.__doc__)  # Some method docs


print(help('re'))  # if module is not imported
print(help(sys))  # if module is imported
print(help(docstrings))  # own module inspection
