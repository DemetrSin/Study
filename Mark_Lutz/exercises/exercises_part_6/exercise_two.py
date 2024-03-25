# Exercise 2

class MyList:
    def __init__(self, data):
        if isinstance(data, MyList):
            self.data = list(data.data[:])
        else:
            self.data = list(data[:])
        self.start = -1
        self.stop = len(self.data) - 1

    def __add__(self, other):
        if isinstance(other, MyList):
            return self.data + other.data
        return self.data + other

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self[self.start]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst1 = MyList(lst)
    print(lst1)  # [1, 2, 3, 4, 5]
    lst2 = MyList(lst1)
    print(lst2)  # [1, 2, 3, 4, 5]

    print(lst1[2:4])  # [3, 4]
    print(lst2[:2])  # [1, 2]
    print(lst[4])  # 5
    print(lst1 + lst2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(lst)  # [1, 2, 3, 4, 5] !!! wasn't touched

    print(lst1.__iter__())  # <generator object MyList.__iter__ at 0x000001E594B0E880>
    print(next(lst1))  # 1
    print(lst1.__next__())  # 2
    print(lst1.__next__())  # 3
    print(lst1.__next__())  # 4
    print(lst1.__next__())  # 5
    # print(lst1.__next__())  # StopIteration
    print()
