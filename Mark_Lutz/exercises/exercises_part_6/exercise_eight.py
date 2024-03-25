class Animal:
    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('Cococo')


class Cat(Mammal):
    def speak(self):
        print('meow')


class Dog(Mammal):
    def speak(self):
        print('gav')


class Primate(Mammal):
    def speak(self):
        print('Uaua')


class Hacker(Primate):
    pass


if __name__ == '__main__':
    spot = Cat()
    spot.reply()  # meow
    spot = Hacker()
    spot.reply()  # Uaua
