import sys
import traceback

try:
    while True:
        while True:
            for i in range(10):
                if i > 1:
                    raise Exception
                print('loop 3')
            print('loop 2')
        print('loop 1')
except Exception:
    print('exception')
    # loop 3
    # loop 3
    # exception

print(i)  # 2 this is from for


class Found(Exception):pass


def founder(lst):
    if 'some' in lst:
        raise Found
    return False


try:
    item = founder([1, 2, 'som'])
except Found:
    print('Operation did well')

print(item)  # False



try:
    item = founder([1, 2, 'some'])
except Found:
    print('Operation did well')  # Operation did well


try:
    file = open('data')
    file.readlines()
except Exception:
    print('Exception')
finally:
    if 'file' in locals() or 'file' in globals():
        file.close()


def inverse(x):
    return 1 / x


try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('badly.exc', 'w'))


def bye():
    sys.exit(40)


try:
    bye()
except:
    print('got it')  # got it

print('continue')  # continue
