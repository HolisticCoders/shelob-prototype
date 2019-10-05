import abc
from typing import List


class AttributeBase:
    def __init__(self, name, attribute_type):
        self.name = name
        self._attribute_type = attribute_type
        self.input = None
        self.outputs = []

    def connect(self, other):
        is_same_class = self.__class__ is other.__class__
        is_same_type = self._attribute_type is other._attribute_type

        if is_same_class and is_same_type:
            self.outputs.append(other)
            other.input = self


class Attribute(AttributeBase):
    def __init__(self, name, attribute_type):
        super().__init__(name, attribute_type)
        self.name = name
        self._attribute_type = attribute_type
        self._value = None

    def get(self):
        return self._value

    def set(self, value):
        if not self._attribute_type.validate(value):
            raise ValueError(
                f"value {value} is not a {self._attribute_type.__class__.__name__}"
            )
        self._value = value


class AttributeArray(AttributeBase):
    def __init__(self, name, attribute_type):
        super().__init__(name, attribute_type)
        self._attributes: List[Attribute] = []

    def __getitem__(self, index):
        return self._attributes[index]

    def __len__(self):
        return len(self._attributes)

    def add_attribute(self):
        new_attribute = Attribute(
            name=f"{self.name}_{len(self._attributes)}",
            attribute_type=self._attribute_type,
        )
        self._attributes.append(new_attribute)
        return new_attribute
    
    def remove_attribute(self, index):
        del self._attributes[index]

    def clear(self):
        self._attributes = []


class AttributeType(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def validate(cls, value):
        pass


class IntAttribute(AttributeType):
    @classmethod
    def validate(cls, value):
        if isinstance(value, int):
            return True
        else:
            return False
