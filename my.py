traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def private(*privates):
    def on_decorator(aClass):
        class OnInstance:
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return OnInstance

    return on_decorator


if __name__ == '__main__':
    traceMe = True


    @private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print(f"{self.label} => {self.data}")


    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])


    print(X.label)
    X.display()
    X.double()
    X.display()
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()
