# Exercise 1
import sys
import traceback


def oops():
    raise IndexError


def hey_oops():
    try:
        oops()
    except IndexError:
        print('caught')


hey_oops()  # caught


# Exercise 2

class MyError(Exception):
    pass


def oops2():
    raise MyError('Smth')


def hey_oops2():
    try:
        oops()
    except (IndexError, MyError) as e:
        print(e)


hey_oops()  # Smth


# Exercise 3

def safe(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception:
        print(sys.exc_info())


safe(oops2)  # (<class '__main__.MyError'>, MyError('Smth'), <traceback object at 0x00000191132811C0>)

# part 2


def safe(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception:
        traceback.print_exc()


# safe(oops)


# decorator ?
def safe_dec(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            print(sys.exc_info())
    return wrapper


@safe_dec
def oops3():
    raise Exception


oops3()  # (<class 'Exception'>, Exception(), <traceback object at 0x000001F4662E2800>)
