class Attribute:
    def __init__(self, name):
        self.name = name
        self._value = None
        self.input = None
        self.outputs = []

    def get(self):
        return self._value

    def set(self, value):
        self._value = value

    def connect(self, other):
        self.outputs.append(other)
        other.input = self
