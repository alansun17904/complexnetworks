from .edge import Edge
from .node import Node


class Graph:
    """
    Generic class for a graph
    """
    def __init__(self, adj_matrix, directed=False):
        self.adj_matrix = adj_matrix
        self.nodes = []
        self.edges = []
        self.directed = directed
        self._initialize_nodes()
        self._initialize_edges()

    def get_node(self, node_name):
        return [n for n in self.nodes if n.name == node_name][0]

    def _initialize_nodes(self):
        for rindex, row in enumerate(self.adj_matrix):
            # find nodes that are adjacent to the current node.
            adj_nodes = [adj_index for adj_index, value in enumerate(self.adj_matrix[rindex]) if value == 1]
            self.nodes.append(Node(rindex, adj_nodes))
        return 1

    def _initialize_edges(self):
        if self.directed:
            for node in self.nodes:
                for adj_node in node.adjancent_nodes:
                    self.edges.append(Edge(node, self.get_node(adj_node)))
        else:
            for row in range(len(self.nodes)):
                for col in range(row, len(self.nodes[row])):
                    self.edges.append(Edge(self.get_node(row), self.get_node(col)))

