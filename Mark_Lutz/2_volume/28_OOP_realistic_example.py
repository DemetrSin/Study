class AttrDisplay:
    def gather_attr(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f"{key} = {getattr(self, key)}")
        return ', '.join(attrs)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.gather_attr()}"


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def pay_rise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __repr__(self):
    #     return f"Person: {self.name}, {self.pay}"


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def pay_rise(self, percent, bonus=.10):
        Person.pay_rise(self, percent + bonus)


class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def pay_rise(self, percent, bonus):
        self.person.pay_rise(percent + bonus)

    def __getattr__(self, item):
        return getattr(self.person, item)

    def __repr__(self):
        return str(self.person)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def pay_rises(self, percent):
        for person in self.members:
            person.pay_rise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)

    print(bob.name, bob.pay)  # Bob Smith 0
    print(sue.name, sue.pay)  # Sue Jones 10000

    print(bob.name.split())  # ['Bob', 'Smith']
    sue.pay *= 1.10
    print(sue.pay)  # 11000.0

    print(bob.last_name(), sue.last_name())  # Smith Jones
    sue.pay_rise(.10)
    print(sue.pay)  # 12100

    print(sue)  # Person: job = dev, name = Sue Jones, pay = 12100

    # Test Manager

    tom = Manager('Tom Jones', 20000)
    print(tom)  # Manager: job = mgr, name = Tom Jones, pay = 20000
    tom.pay_rise(.10)
    print(tom.last_name())  # Jones
    print(tom)  # Manager: job = mgr, name = Tom Jones, pay = 24000

    print('---All Three---')
    for obj in (bob, sue, tom):
        obj.pay_rise(.10)
        print(obj)

    development = Department(bob, sue)
    development.add_member(tom)
    development.pay_rises(.10)
    development.show_all()

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


x, y = TopTest(), SubTest()
print(x)  # TopTest: attr1 = 0, attr2 = 1
print(y)  # SubTest: attr1 = 2, attr2 = 3


# Shelve
import shelve

db = shelve.open('persondb')
for obj in(bob, sue, tom):
    db[obj.name] = obj

db.close()

import glob

print(glob.glob('person*'))  # ['persondb.bak', 'persondb.dat', 'persondb.dir']

db = shelve.open('persondb')
print(len(db))  # 3
print(list(db.keys()))  # ['Bob Smith', 'Sue Jones', 'Tom Jones']
bob = db['Bob Smith']
print(bob)  # Person: job = None, name = Bob Smith, pay = 0
print(bob.last_name())  # Smith
for key in db:
    print(f"{key} => {db[key]}")
    # Bob Smith => Person: job = None, name = Bob Smith, pay = 0
    # Sue Jones => Person: job = dev, name = Sue Jones, pay = 14641
    # Tom Jones => Manager: job = mgr, name = Tom Jones, pay = 34560

for key in sorted(db):
    print(f"{key} => {db[key]}")

sue = db['Sue Jones']
sue.pay_rise(.10)
db['Sue Jones'] = sue
db.close()
