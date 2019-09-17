import pytest

from shelob.core.graph import Graph


def test_create_graph():
    Graph()


def test_add_node():
    graph = Graph()
    graph.add_node("MyNode")
    assert len(graph.nodes) == 1


def test_add_conflicting_node():
    graph = Graph()
    graph.add_node("MyNode")
    with pytest.raises(RuntimeError):
        graph.add_node("MyNode")


def test_delete_node():
    graph = Graph()
    graph.add_node("MyNode")
    graph.delete_node("MyNode")
    assert len(graph.nodes) == 0


def test_delete_inexistant_node():
    graph = Graph()
    with pytest.raises(RuntimeError):
        graph.delete_node("MyNode")

