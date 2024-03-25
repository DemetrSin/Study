# Exercise 7

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(food_name, self.employee)

    def result(self):
        self.customer.print_food()


class Customer:
    def __init__(self, dish=None):
        self.dish = dish

    def place_order(self, food_name, employee):
        self.dish = employee.take_order(food_name)

    def print_food(self):
        print(self.dish.name)


class Employee:
    def take_order(self, food_name):
        return Food(food_name)


class Food:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    lunch = Lunch()
    lunch.order('shaurma')
    lunch.result()  # shaurma
    lunch.order('soup')
    lunch.result()  # soup
