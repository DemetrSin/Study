class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f"Person: {self.name}, {self.pay}"


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)

    def __getattr__(self, attr):
        print(attr)
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


sue = Person('Sue', 'dev', 10000)
tom = Manager('Tom', 5000)
print(tom.last_name())









