
# Methods Comparison

# Property


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square ** 2

    def set_square(self, value):
        self._square = value

    square = property(get_square, set_square)

    def get_cube(self):
        return self._cube ** 3

    cube = property(get_cube)


x = Powers(3, 4)
print(x.square, x.cube)  # 9 64
x.square = 5
print(x.square)  # 25


# Descriptors



