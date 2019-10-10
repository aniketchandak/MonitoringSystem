class Observable:
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)

    def unsubscribe(self, observer):
        self.observers.discard(observer)

    def notify(self, arg=None):
        for each in self.observers:
            each.update(arg)
