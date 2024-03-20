# Delegation


class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        print('Trace: ' + attr)
        return getattr(self.obj, attr)


x = Wrapper([1, 2, 3])
x.append(4)  # Trace: append
print(x.obj)  # [1, 2, 3, 4]

x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))


# Pseudo-closed

