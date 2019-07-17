class Node:
    def __init__(self, name, state, adjacent_nodes):
        self.name = name
        self.state = state
        self.adjancent_nodes = adjacent_nodes
        self.pending_state = None

    def flip_pending_state(self):
        if self.pending_state is not None:
            self.state = self.pending_state
            self.pending_state = None

    def __str__(self):
        return self.name