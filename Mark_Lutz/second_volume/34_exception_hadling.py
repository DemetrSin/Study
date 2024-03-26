def division(a, b):
    print(a / b)


def ongoing(a):
    print(division(a, 0))


# ongoing(2)  # ZeroDivisionError: division by zero


def kaboom(x, y):
    print(x + y)


try:
    kaboom([1, 2, 3], 'spam')
except Exception:
    print('exception')  # exception

print('ongoing')  # ongoing


class MyError(Exception):
    pass


def stuff(file):
    raise MyError


file = open('data', 'w')

try:
    # stuff(file)  # MyError
    pass
finally:
    file.close()

print('unreachable')


try:
    raise IndexError
except IndexError:
    # raise MyError
    pass
except MyError:  # not working
    pass
finally:
    print('I will work)')  # I will work)


try:
    raise IndexError
except MyError:  # working
    pass
except IndexError:
    # raise MyError
    pass

finally:
    print('I will work)')  # I will work)


try:
    print('try run')  # try run
except:
    print('except run')
else:
    print('else run')  # else run
finally:
    print('finally run')  # finally run


# raise Exception
# raise Exception()

exc = Exception
# raise exc
# raise exc()
exc = Exception()
# raise exc

excs = [IndexError, TypeError]
# raise excs  # TypeError: exceptions must derive from BaseException
# raise excs[0]  # IndexError

x = 99

try:
    1 / 0
except Exception as x:  # localize and delete x !!
    print(x)  # division by zero

# print(x)  # NameError: name 'x' is not defined

x = 99
print({x for x in 'spam'})  # {'m', 'a', 's', 'p'} only localize  !!!
print(x)  # 99

x = 99
for x in 'spam':  # localize and overwrite x !!!
    print(x, end=' ')   # s p a m

print(x)  # m


try:
    1 / 0
except Exception as x:
    save = x

print(save)  # division by zero


try:
    raise IndexError('spam')
except IndexError:
    print('propagating')
    # raise   # IndexError: spam


try:
    1 /0
except Exception as e:
    # The above exception was the direct cause of the following exception:
    # raise TypeError('bad') from e  # TypeError: bad
    pass


try:
    1 / 0
except:
    # During handling of the above exception, another exception occurred:
    # badname  # NameError: name 'badname' is not defined
    pass


try:
    try:
        raise IndexError
    except Exception as e:
        raise TypeError() from e
except Exception as e:
    # raise SyntaxError() from e  # SyntaxError: None
    pass


try:
    try:
        1/0
    except:
        badname
except:
    # open('bad')  # FileNotFoundError: [Errno 2] No such file or directory: 'bad'
    pass


#  assert

def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


# f(2)  # AssertionError: x must be negative


# with

with open('data') as data, open('res', 'w') as res:
    for line in data:
        if 'some' in line:
            res.write(line)


with open('data') as data, open('res', 'w') as res:
    for pair in zip(data, res):
        print(pair)


with open('data') as data, open('res', 'w') as res:
    for (line_num, (line1, line2)) in zip(data, res):
        print(line_num, line, line2)
