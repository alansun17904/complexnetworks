import random


class Edge:
    def __init__(self, node1, node2, q=0):
        self.node1 = node1
        self.node2 = node2
        self.q = q

    def flip_coin(self):
        return True if random.random() < self.q else False
