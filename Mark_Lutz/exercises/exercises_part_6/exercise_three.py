from exercise_two import MyList


class MylistSub(MyList):
    count = 0

    def __init__(self, data):
        self.instance_count = 0
        super().__init__(data)

    def __add__(self, other):
        print('add')
        MylistSub.count += 1
        self.instance_count += 1
        return super().__add__(other)

    def stats(self):
        print(self.count, self.instance_count)


if __name__ == '__main__':
    x = MylistSub('spam')
    y = MylistSub('eggs')
    print(x[:2])  # ['s', 'p']
    print(y[1:3])  # ['g', 'g']
    print(x[3])  # m
    print(x + [1, 2])  # ['s', 'p', 'a', 'm', 1, 2]
    x.stats()  # 1 1
    y.stats()  # 1 0
    print(x + ['egg'])  # ['s', 'p', 'a', 'm', 'egg']
    print(y + ['bar'])  # ['e', 'g', 'g', 's', 'bar']
    x.stats()  # 3 2
    y.stats()  # 3 1








