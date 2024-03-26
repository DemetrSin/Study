import sys


class General(Exception): pass
class Specific1(General):pass
class Specific2(General): pass


def raiser():
    x = General()
    raise x


def raiser2():
    x = Specific1()
    raise x


def raiser3():
    x = Specific2
    raise x


for x in (raiser, raiser2, raiser3):
    try:
        x()
    except General:
        print(f"caught: {sys.exc_info()[0]}")  # Output:
        # caught: <class '__main__.General'>
        # caught: <class '__main__.Specific1'>
        # caught: <class '__main__.Specific2'>


try:
    1/0
except:
    print(sys.exc_info())
    # (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x0000022926D423C0>)


class General(Exception): pass
class Specific1(General):pass
class Specific2(General): pass
def raiser():raise General
def raiser2():raise Specific1
def raiser3():raise Specific2


for func in (raiser, raiser2, raiser3):
    try:
        func()
    except General as e:
        print(f"caught: {e.__class__}")
        # caught: <class '__main__.General'>
        # caught: <class '__main__.Specific1'>
        # caught: <class '__main__.Specific2'>


i = IndexError('spam', 'eggs', 234)
print(i.args)  # ('spam', 'eggs', 234)
print(i)  # ('spam', 'eggs', 234)
# raise i  # IndexError: ('spam', 'eggs', 234)


class E(Exception): pass


e = E('spam')
print(e)  # spam
print(e.args)  # ('spam',)
print(repr(e))  # E('spam')


class OwnException(Exception):
    def __str__(self):
        return 'This is Own created Exception'


try:
    raise OwnException
except OwnException as e:
    print(e)  # This is Own created Exception

# raise OwnException  # OwnException: This is Own created Exception


class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file


def parser():
    raise FormatError(42, file='some.txt')


try:
    parser()
except FormatError as e:
    print(f"Error at line:{e.line} in file:{e.file}")  # Error at line:42 in file:some.txt


class FormatError(Exception):
    log_file = 'format_error.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def log_error(self):
        log = open(self.log_file, 'a')
        print('Error at : ', self.file, self.line, file=log)


def parser():
    raise FormatError(40, 'spam.txt')


try:
    parser()
except FormatError as e:
    e.log_error()
