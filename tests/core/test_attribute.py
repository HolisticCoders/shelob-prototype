import pytest

from shelob.core.attribute import Attribute, AttributeArray


def test_get_attribute_value(int_attribute_type):
    attribute = Attribute("attribute", int_attribute_type)
    attribute.get()


def test_set_attribute_value(int_attribute_type):
    attribute = Attribute("attribute", int_attribute_type)
    attribute.set(10)
    assert attribute.get() == 10


def test_set_invalid_attribute_value(int_attribute_type):
    attribute = Attribute("attribute", int_attribute_type)
    with pytest.raises(ValueError):
        attribute.set("Invalid")


def test_add_connection(int_attribute_type):
    attribute1 = Attribute("attribute1", int_attribute_type)
    attribute2 = Attribute("attribute1", int_attribute_type)
    attribute1.connect(attribute2)

    assert attribute2 in attribute1.outputs and attribute2.input is attribute1


def test_add_attribute_array(int_attribute_type):
    attribute = AttributeArray("attribute_array", int_attribute_type)
    attribute.add_attribute()
    assert len(attribute) == 1


def test_remove_attribute_array(int_attribute_type):
    attribute = AttributeArray("attribute_array", int_attribute_type)
    attribute.add_attribute()
    attribute.remove_attribute(0)
    assert len(attribute) == 0


def test_clear_attribute_array(int_attribute_type):
    attribute = AttributeArray("attribute_array", int_attribute_type)
    attribute.add_attribute()
    attribute.clear()
    assert len(attribute) == 0


def test_get_set_attribute_array(int_attribute_type):
    attribute = AttributeArray("attribute_array", int_attribute_type)
    attribute.add_attribute()
    attribute[0].set(10)
    assert attribute[0].get() == 10


def test_set_invalid_attribute_array(int_attribute_type):
    attribute = AttributeArray("attribute_array", int_attribute_type)
    attribute.add_attribute()
    with pytest.raises(ValueError):
        attribute[0].set("Invalid")
