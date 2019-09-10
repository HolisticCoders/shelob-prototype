from shelob.core.attribute import Attribute


def test_get_attribute_value():
    attribute = Attribute("attribute")
    attribute.get()


def test_set_attribute_value():
    attribute = Attribute("attribute")
    attribute.set(10)
    assert attribute.get() == 10


def test_add_connection():
    attribute1 = Attribute("attribute1")
    attribute2 = Attribute("attribute2")
    attribute1.connect(attribute2)

    assert attribute2 in attribute1.outputs and attribute2.input is attribute1
