import sys
print(sys.getrefcount(45))
a = 45
b = '45'


def forty_five():
    return 45


print(id(a), id(int(b)), id(forty_five()))   # They are equal because of python cash


a = ['spam']
b = a
b[0] = 'shrubbery'

print(a)
print(sys.argv)
