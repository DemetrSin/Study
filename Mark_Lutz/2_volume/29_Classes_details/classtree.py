def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for superclass in cls.__bases__:
        classtree(superclass, indent + 3)


def instance_tree(inst):
    print(f"Tree of {inst}")
    classtree(inst.__class__, 3)


def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instance_tree(B())
    instance_tree(F())


class Emp: pass


class Person(Emp): pass


bob = Person()


if __name__ == '__main__':
    selftest()
    instance_tree(bob)