import sys
import time
import timeit

sys.set_int_max_str_digits(1000000)

# def timer(func, *args):
#     start = time.perf_counter()
#     for i in range(1000):
#         func(*args)
#     return time.perf_counter() - start
#
#
# print(timer(pow, 2, 1000))  # 0.0004008999967481941
# print(timer(str.upper, 'spam'))  # 2.889998722821474e-05

timer = time.perf_counter if sys.platform[:3] == 'win' else time.time


def total(reps, func, *args, **kwargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(reps, func, *args, **kwargs):
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def best_of_total(reps1, reps2, func, *args, **kwargs):
    return bestof(reps1, total, reps2, func, *args, **kwargs)


print(total(1000, pow, 2, 1000)[0])  # 0.00039610001840628684
print(total(1000, str.upper, 'spam'))  # (3.5500008380040526e-05, 'SPAM')
print(bestof(1000, str.upper, 'spam'))  # (0.0, 'SPAM')
print(bestof(1000, pow, 2, 1000000)[0])  # 0.0019893999851774424


# Keep going


def total(func, *args, **kwargs):
    _reps = kwargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, ret


def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return best, ret


def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))


print(total(pow, 2, 1000)[0])  # 0.00038640000275336206
print(total(pow, 2, 1000, _reps=1000)[0])  # 0.0003725999849848449
print(total(pow, 2, 1000, _reps=1000000)[0])  # 0.3913499999907799
print(bestof(pow, 2, 1000000)[0])  # 0.0020003000099677593
print(bestof(pow, 2, 1000000, _reps=30)[0])  # 0.0019982000230811536

# Func

x = 99


def selector():
    print(x)
    x = 88


try:
    selector()  # UnboundLocalError:
except UnboundLocalError:
    pass


# OR

x = 77


def selector():
    import __main__
    print(__main__.x)
    x = 88
    print(x)


selector()  # 77 and then 88


def saver(x=[]):
    x.append(1)
    print(x)


saver()  # [1]
saver()  # [1, 1]
saver()  # [1, 1, 1]
saver([2])  # [2, 1]


def saver(x=None):
    if not x:
        x = []
    x.append(1)
    print(x)


saver()  # [1]
saver()  # [1]
saver([2])  # [2, 1]


def saver():
    saver.x.append(1)
    print(saver.x)


saver.x = []
saver()  # [1]
saver()  # [1, 1]
saver()  # [1, 1, 1]


def proc(x):
    print(x)


f = proc('some')  # some
print(f)  # None
proc('spam')  # spam
