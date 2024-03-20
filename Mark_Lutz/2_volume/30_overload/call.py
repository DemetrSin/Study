# __call__


class Callee:
    def __call__(self, *args, **kwargs):
        print('Called: ', args, kwargs)


c = Callee()
c(1, 2, 3)  # Called:  (1, 2, 3) {}
c(1, 2, 3, x=24, y=345)  # Called:  (1, 2, 3) {'x': 24, 'y': 345}


class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value ** other


p = Prod(5)
print(p(9))  # 1953125


class Color:
    def __init__(self, value):
        self.value = value

    def __call__(self):
        print(f"turn in {self.value}")


c = Color('green')
c()  # turn in green


def color_f(color):
    def nested():
        print(f"turn in {color}")
    return nested


col = color_f('red')
col()  # turn in red

col2 = (lambda color='red': 'turn ' + color)
print(col2())  # turn red


class Callback:
    def __init__(self, color):
        self.color = color

    def change_color(self):
        print('turn in ', self.color)


class Button:
    def __init__(self, command):
        self.command = command

    def __call__(self):
        return self.command()


cb1 = Callback('black')
cb2 = Callback('white')
b1 = Button(command=cb1.change_color)
b2 = Button(command=cb2.change_color)
cb1.change_color()  # turn in  black
b1()  # turn in  black
b2()  # turn in  white
