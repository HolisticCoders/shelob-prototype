import pytest

from shelob.core.node import Node


def test_add_attribute():
    node = Node("Node01")
    node.add_attribute("output")
    assert node._attributes.get("output") is not None


def test_add_conflicting_attribute():
    node = Node("Node01")
    node.add_attribute("output")
    with pytest.raises(RuntimeError):
        node.add_attribute("output")


def test_delete_attribute():
    node = Node("Node01")
    node.add_attribute("output")
    node.delete_attribute("output")
    assert node._attributes.get("output") is None


def test_delete_inexistant_attribute():
    node = Node("Node01")
    with pytest.raises(AttributeError):
        node.delete_attribute("output")


def test_get_attribute():
    node = Node("Node01")
    node.add_attribute("output")
    assert node.output.name == "output"


def test_set_attribute():
    node = Node("Node01")
    node.add_attribute("output")
    node.output.set(10)
    assert node.output.get() == 10

