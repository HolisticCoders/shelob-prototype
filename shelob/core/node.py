from shelob.core.attribute import Attribute


class Node:
    def __init__(self, name=None):
        self.name = name
        self._attributes = {}

    def __getattr__(self, name):
        attribute = getattr(self, "_attributes").get(name)
        if attribute is None:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
        return attribute

    def add_attribute(self, attribute_name):
        if attribute_name in self._attributes:
            raise RuntimeError(
                f"Attribute {attribute_name} already exists on {self.name}"
            )
        attribute = Attribute(attribute_name)
        self._attributes[attribute_name] = attribute

    def delete_attribute(self, attribute_name):
        if not attribute_name in self._attributes:
            raise AttributeError("{self.name} has no attribute {attribute_name}")

        del self._attributes[attribute_name]

