# 5 kyu Simple Events
# https://www.codewars.com/kata/52d3b68215be7c2d5300022f

class Event():
    def __init__(self):
        self.handler = []

    def subscribe(self, handler):
        self.handler.append(handler)

    def unsubscribe(self, handler):
        self.handler.remove(handler)

    def emit(self, *args):
        self.handler[-1](*args)


if __name__ == '__main__':
    event = Event()


    class Testf():
        def __init__(self):
            self.calls = 0
            self.args = []

        def __call__(self, *args):
            self.calls += 1
            self.args += args


    f = Testf()

    event.subscribe(f)
    event.emit(1, 'foo', True)

    print(f.calls, 1)  # calls a handler
    print(f.args, [1, 'foo', True])  # passes arguments

    event.unsubscribe(f)
    event.emit(2)

    print(f.calls, 1)  # no second call