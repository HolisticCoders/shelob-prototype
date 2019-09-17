from shelob.core.node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name in self.nodes:
            raise RuntimeError(f"A Node with the name {name} already exists")
        new_node = Node(name)
        self.nodes[name] = new_node

    def delete_node(self, name):
        if name not in self.nodes:
            raise RuntimeError(f"Node {name} does not exist and cannot be deleted")
        del self.nodes[name]
