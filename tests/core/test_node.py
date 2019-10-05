import pytest

from shelob.core.node import Node


def test_add_attribute(int_attribute_type):
    node = Node("Node01")
    node.add_attribute("output", int_attribute_type)
    assert node._attributes.get("output") is not None


def test_add_conflicting_attribute(int_attribute_type):
    node = Node("Node01")
    node.add_attribute("output", int_attribute_type)
    with pytest.raises(RuntimeError):
        node.add_attribute("output", int_attribute_type)


def test_delete_attribute(int_attribute_type):
    node = Node("Node01")
    node.add_attribute("output", int_attribute_type)
    node.delete_attribute("output")
    assert node._attributes.get("output") is None


def test_delete_inexistant_attribute():
    node = Node("Node01")
    with pytest.raises(RuntimeError):
        node.delete_attribute("output")


def test_get_attribute(int_attribute_type):
    node = Node("Node01")
    node.add_attribute("output", int_attribute_type)
    assert node.output.name == "output"


def test_set_attribute(int_attribute_type):
    node = Node("Node01")
    node.add_attribute("output", int_attribute_type)
    node.output.set(10)
    assert node.output.get() == 10

