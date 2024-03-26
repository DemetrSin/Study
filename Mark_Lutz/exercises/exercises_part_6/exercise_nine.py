class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        for action in (self.customer, self.clerk, self.parrot):
            print(f"{action.__class__.__name__}: {action.line()}")


class Customer:
    def line(self):
        return 'that\'s one ex-bird'


class Clerk:
    def line(self):
        return 'no, it isn\'t'


class Parrot:
    def line(self):
        return None


scene = Scene()
scene.action()
