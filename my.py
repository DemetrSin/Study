# Exercise 2

class MyList(list):
    def __init__(self, data):
        if isinstance(data, MyList):
            self.data = data.data[:]
        self.data = data[:]

    # def __str__(self):
    #     return str(self.data)


lst = [1, 2, 3, 4, 5]
lst1 = MyList(lst)
print(lst1.data)  # [1, 2, 3, 4, 5]
print(lst1)
lst2 = MyList(lst1)
print(lst2.data)







