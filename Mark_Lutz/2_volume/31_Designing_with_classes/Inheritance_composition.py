# Inheritance
import sys


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, ' does something')

    def __repr__(self):
        return f"Employee: name={self.name}, salary={self.salary}"


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, ' makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, ' interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, ' makes pizza')


bob = PizzaRobot('Bob')
print(bob)  # Employee: name=Bob, salary=50000
bob.work()  # Bob  makes pizza
bob.give_raise(0.20)
print(bob)  # Employee: name=Bob, salary=60000.0
print()
for klass in Employee, Chef, Server, PizzaRobot:
    obj = klass(klass.__name__)
    obj.work()
"""Output:
Employee  does something
Chef  makes food
Server  interfaces with customer
PizzaRobot  makes pizza
"""
print('\n'*5)


# Composition

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f"{self.name} orders from {server}")

    def pay(self, server):
        print(f"{self.name} pays for item to {server}")


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


scene = PizzaShop()
scene.order('Homer')
print('...')
scene.order('Shaggy')
"""Output:
Homer orders from Employee: name=Pat, salary=40000
Bob  makes pizza
oven bakes
Homer pays for item to Employee: name=Pat, salary=40000
...
Shaggy orders from Employee: name=Pat, salary=40000
Bob  makes pizza
oven bakes
Shaggy pays for item to Employee: name=Pat, salary=40000
"""


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'Converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


obj = Uppercase(open('t.txt'), sys.stdout)
# obj.process()