import random


class Edge:
    def __init__(self, node1, node2, q=0):
        """
        :param node1: Node object
        :param node2: Node object
        :param q: edge probability
        """
        self.node1 = node1
        self.node2 = node2
        self.q = q  # weight of the edge / probability
        self.cant_use = False

    def flip_coin(self):
        return True if random.random() < self.q else False
