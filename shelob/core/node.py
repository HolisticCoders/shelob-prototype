from shelob.core.attribute import Attribute


class Node:
    def __init__(self, name):
        self.name = name
        self._attributes = {}

    def __getattr__(self, name):
        attribute = getattr(self, "_attributes").get(name)
        if attribute is None:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
        return attribute

    def add_attribute(self, name):
        if name in self._attributes:
            raise RuntimeError(f"Attribute {name} already exists on {self.name}")
        attribute = Attribute(name)
        self._attributes[name] = attribute

    def delete_attribute(self, name):
        if not name in self._attributes:
            raise RuntimeError("Node {self.name} has no attribute {name}")

        del self._attributes[name]

