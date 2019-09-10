from shelob.core.graph import Graph


def test_create_graph():
    Graph()


def test_add_node():
    graph = Graph()
    graph.add_node()
    assert len(graph.nodes) == 1

