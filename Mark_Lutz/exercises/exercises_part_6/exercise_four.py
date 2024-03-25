# Exercise 4

class Attrs:
    # def __getattribute__(self, item):
    #     print(f"getattribute {item}")

    def __getattr__(self, item):
        print(f"getattr {item}")

    def __setattr__(self, key, value):
        print(f"setattr {key} > {value}")


if __name__ == '__main__':
    attr = Attrs()
    attr.smth  # getattr smth
    attr.a = 21  # setattr a > 21
    Attrs.lst = [1, 2, 3, 4, 5]  # setattr lst > [1, 2, 3, 4, 5]
    attr.lst = [1, 2, 3, 4, 5]  # setattr lst > [1, 2, 3, 4, 5]
    attr.lst  # getattribute lst
    getattr(attr, 'lst', 0)  # getattribute lst
