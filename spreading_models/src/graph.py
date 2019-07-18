from .edge import Edge
from .node import Node


class Graph:
    """
    Generic class for a graph
    """
    def __init__(self, num_nodes, edge_tuple, directed=False):
        self.num_nodes = num_nodes
        self.edge_tuple = edge_tuple
        self.nodes = []
        self.edges = []
        self.directed = directed
        self._make_adj_matrix()
        self._initialize_nodes()
        self._initialize_edges()

    def _make_adj_matrix(self):
        self.adj = [[0 for col in range(self.num_nodes)] for row in range(self.num_nodes)]
        for edge in self.edges_tuple:
            if not self.directed:
                self.adj[edge[0]][edge[1]] = 1  # undirected graph
                self.adj[edge[1]][edge[0]] = 1  # start node -> end node set to 1 as well as end node -> start node
            else:
                self.adj[edge[0]][edge[1]] = 1
        return self.adj

    def get_node(self, node_name):
        return [n for n in self.nodes if n.name == node_name][0]

    def _initialize_nodes(self):
        for rindex, row in enumerate(self.adj_matrix):
            # find nodes that are adjacent to the current node.
            adj_nodes = [adj_index for adj_index, value in enumerate(self.adj_matrix[rindex]) if value == 1]
            self.nodes.append(Node(rindex, adj_nodes))
        return 1

    def _initialize_edges(self):
        if self.directed:  # in directed graphs the order matters so must loop through entire matrix
            for node in self.nodes:
                for adj_node in node.adjancent_nodes:
                    self.edges.append(Edge(node, self.get_node(adj_node)))
        else:
            # loop through only half of the matrix not including the diagnol
            for row in range(len(self.nodes)):
                for col in range(row, len(self.nodes[row])):
                    self.edges.append(Edge(self.get_node(row), self.get_node(col)))  # add Edge objects to self.edge

