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

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3


class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


x = Powers(3, 4)
print(x.square, x.cube)  # 9 64
x.square = 5
print(x.square)  # 25

# __getattr__


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, attr):
        if attr == 'square':
            return self._square ** 2
        elif attr == 'cube':
            return self._cube ** 3
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        if attr == 'square':
            self.__dict__['_' + attr] = value
        elif attr == 'cube':
            self.__dict__['_' + attr] = value
        else:
            self.__dict__[attr] = value


x = Powers(3, 4)
print(x.square, x.cube)  # 9 64
x.square = 5; x.cube = 6
print(x.square, x.cube)  # 25 216


#  __getattribute__

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, attr):
        if attr == 'square':
            return object.__getattribute__(self, '_' + attr) ** 2
        elif attr == 'cube':
            return object.__getattribute__(self, '_' + attr) ** 3
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):
        if attr == 'square':
            object.__setattr__(self, '_' + attr, value)
        elif attr == 'cube':
            object.__setattr__(self, '_' + attr, value)
        else:
            object.__setattr__(self, attr, value)


x = Powers(3, 4)
print(x.square, x.cube)  # 9 64
x.square = 5; x.cube = 6
print(x.square, x.cube)  # 25 216
