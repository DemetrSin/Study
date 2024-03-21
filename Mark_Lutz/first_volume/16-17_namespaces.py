import builtins


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


print(intersect('spam', 'scam'))  # ['s', 'a', 'm']
print([x for x in 'spam' if x in 'scam'])  # ['s', 'a', 'm']
print(set('spam') & set('scam'))  # {'s', 'a', 'm'}
print(intersect([1, 2, 3], (1, 4)))  # [1] -- Polymorphism


# Chapter 17

# print(dir(builtins))
x = 88


def func():
    global x
    x = 99


print(x)  # 88
func()
print(x)  # 99

y, z = 1, 2


def all_global():
    global n
    n = y + z


all_global()
print(n)  # 3


d = {1: 'a', 3: 'c'}
d[2] = 'b'
print(d)  # {1: 'a', 3: 'c', 2: 'b'}


# Test

var = 99


def local():
    var = 0


def glob1():
    global var
    var += 1


def glob2():
    var = 0
    oh.var += 1


def glob3():
    var = 0
    import sys
    glob = sys.modules['oh']
    glob.var += 1


def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)


test()


# Keep going


x = 99


def f1():
    x = 88

    def f2():
        print(x)
    f2()


f1()  # 88


def f1():
    x = 88

    def f2():
        print(x)
    return f2


action = f1()
action()  # 88

# Next

def maker(n):
    def action(x):
        return x ** n
    return action


f = maker(2)  # It remembers 2
print(f)  # <function maker.<locals>.action at 0x000001B714406C00>
print(f(4))  # 16 The call
g = maker(3)  # It remembers 3
print(g(3))  # 27
print(f(3))  # 9

# OR


def maker2(n):
    return lambda x: x ** n


y = maker(4)
print(y(5))  # 625


# Without nested func


def f1(x=77):
    f2(x)


def f2(x):
    print(x)


f1()  # 77

# lambda option


def func(x):
    action = lambda n: x ** n
    return action


x = func(4)
print(x(2))  # 16


def make_actions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts


acts = make_actions()
print(acts[0](2))  # 0
print(acts[2](2))  # 4


def tester(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1
    return nested


t = tester(2)
try:
    print(t('aps'))  # UnboundLocalError
except UnboundLocalError:
    pass


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


t = tester(3)
print(t('oil'))  # oil 3
print(t('ham'))  # ham 4
print(t('sam'))  # sam 5
g = tester(3)
print(g('spam'))  # spam 3


# with attribute


def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested


f = tester(0)
print(f('spam'))  # spam 0
print(f('spam'))  # spam 1
print((f.state))  # 2
g = tester(41)
print(g('spam'))  # spam 41
print(g('spam'))  # spam 42
print(g.state)  # 43
print(f('spam'))  # spam 2
print(f.state)  # 3


def make_open(id):
    original = builtins.open

    def custom(*args, **kwargs):
        print(f"Custom open call {id}", args, kwargs)
        return original(*args, **kwargs)
    builtins.open = custom


make_open('spam')  # Custom open call eggs ('two.py',) {}
f = open('two.py')  # Custom open call spam ('two.py',) {}
print(len(f.read()))  # 1
make_open('eggs')  # Custom open call eggs ('two.py',) {}
f = open('two.py')  # Custom open call spam ('two.py',) {}
f.close()


