class A: pass
class B: pass


A.a = 1
A.b = 2
A.c = 3
B.a = A.a + A.b + A.c
for A.i in range(B.a):
    print(A.i, end=',')  # 0,1,2,3,4,5,


# mutable

class C:
    shared = []

    def __init__(self):
        self.temp = []


x = C()
y = C()
print(x.shared, x.temp)  # [] []
x.shared.append('spam')
x.temp.append('spam')
print(x.shared, x.temp)  # ['spam'] ['spam']
print(y.shared, y.temp)  # ['spam'] []
print(C.shared)  # ['spam']


# multiple inheritance

class Some:
    def __str__(self):
        return 'Some'

    def other(self):
        print('Some Other')


class Spam:
    def __str__(self):
        return 'Spam'

    def other(self):
        print('Spam Other')


class Super(Some, Spam):
    pass


sup = Super()
sup.other()  # Some Other
Super.other = Spam.other
sup.other()  # Spam Other


# OR


class Super(Some, Spam):
    other = Spam.other


sup = Super()
sup.other()  # Spam Other


# namespace

def generate(label):
    class Spam:
        count = 1

        def method(self):
            print(label, Spam.count)

    return Spam


aclass = generate('Class')
a = aclass()
a.method()  # Class 1
