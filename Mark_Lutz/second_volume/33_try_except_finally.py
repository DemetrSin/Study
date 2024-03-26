def fetcher(obj, index):
    print(obj[index])


def catcher(obj, index):
    try:
        fetcher(obj, index)
    except IndexError:
        print('got error')
    finally:
        print('we are going forward')
    print('continue')


catcher('spam', 3)  # mwe    are going forward    continue
catcher('spam', 4)  # got error    we are going forward   continue


def error():
    try:
        raise IndexError
    except IndexError:
        print('got exception')


error()  # got exception


class AlreadyGotOne(Exception):
    pass


def grail():
    raise AlreadyGotOne


try:
    grail()
except AlreadyGotOne:
    print('small trick')  # small trick


class Career(Exception):
    def __str__(self):
        return 'It\'s not easy to be a programmer for real)'


# raise Career  # Career: It's not easy to be a programmer for real)
# raise Career()  # Career: It's not easy to be a programmer for real)


def after():
    try:
        fetcher('spam', 4)
    finally:
        print('after fetch')
    print('after try?')


# after()  # after fetch
