from graph import Graph
import random


class SiS(Graph):
    def __init__(self, num_nodes, edge_tuple, starting_nodes, alpha, beta, directed):
        super(SiS, self).__init__(num_nodes, edge_tuple, directed)
        self.a = alpha
        self.b = beta
        self.starting_nodes = starting_nodes

        for node in self.nodes:
            if node.name in self.starting_nodes:
                node.state = 1


    def decide(self, node):
        if node.state == 0:
            node.pending_state = 1 if random.random() < self.b else None
        elif node.state == 1:
            node.pending_state = 0 if random.random() < self.a else None

