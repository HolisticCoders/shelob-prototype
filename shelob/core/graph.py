from shelob.core.node import Node


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self):
        new_node = Node()
        self.nodes.append(new_node)

