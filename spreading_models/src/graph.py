from edge import Edge
from node import Node


class Graph:
    """
    Generic class for a graph
    """
    def __init__(self, num_nodes, edge_tuple, directed=False):
        """

        :param num_nodes: Number of nodes in the graph
        :param edge_tuple: A list of tuples or lists that contains the start and end nodes that make up
        the edges.
        :param directed: True if the graph is directed, False if the graph is not directed.
        """
        self.num_nodes = num_nodes
        self.edge_tuple = edge_tuple
        self.nodes = {}
        self.edges = []
        self.directed = directed
        self.edge_dict = {}
        self._make_adj_matrix()
        self._initialize_nodes()
        self._initialize_edges()

    def _make_adj_matrix(self):
        self.adj = [[0 for col in range(self.num_nodes)] for row in range(self.num_nodes)]
        for edge in self.edge_tuple:
            if not self.directed:
                self.adj[edge[0]][edge[1]] = 1  # undirected graph
                self.adj[edge[1]][edge[0]] = 1  # start node -> end node set to 1 as well as end node -> start node
            else:
                self.adj[edge[0]][edge[1]] = 1
        return self.adj

    def _initialize_nodes(self):
        for rindex, row in enumerate(self.adj):
            # find nodes that are adjacent to the current node.
            adj_nodes = [adj_index for adj_index, value in enumerate(self.adj[rindex]) if value == 1]
            self.nodes[rindex] = Node(rindex, adj_nodes)
        return 1

    def _initialize_edges(self):
        if self.directed:  # in directed graphs the order matters so must loop through entire matrix
            for node in self.nodes.values():
                for adj_node in node.adjancent_nodes:
                    self.edges.append(Edge(node, self.nodes[adj_node], directed=True))
        else:
            # loop through only half of the matrix not including the diagonal
            for row in range(len(self.adj)):
                for col in range(row, len(self.adj[row])):
                    # add Edge objects to self.edge
                    if self.adj[row][col] == 1:
                        self.edges.append(Edge(self.nodes[row], self.nodes[col]))


