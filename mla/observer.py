class Signal:
    def __init__(self, name):
        self.name = name
        self.handlers = []

    def connect(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)

    def remove(self, handler):
        if handler in self.handlers:
            self.handlers.remove(handler)

    def remove_all(self):
        self.handlers = []

    def fire(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)
