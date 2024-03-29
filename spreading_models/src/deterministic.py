from graph import Graph


class DeterministicGraph(Graph):
    """
    Models the deterministic model of a node.
    """
    def __init__(self, q, starting_nodes, num_nodes, edge_tuple):
        """
        :param q: The minimum percentage of adjacent nodes for the current node to be infected.
        :param starting_nodes: A list of ints with the names of the starting nodes
        :param num_nodes: The number of nodes in the matrix
        :param edge_tuple: a tuple or list of edges [(a, b), (b, c)] where a and b are node numbers
        """
        super(DeterministicGraph, self).__init__(num_nodes, edge_tuple, directed=False)
        self.starting_nodes = starting_nodes
        self.q = q
        # Initialize the state of the nodes with the starting_nodes list
        for node in self.nodes:
            if node.name in self.starting_nodes:
                node.state = 1

    def decide(self, node):
        """
        :param node: The node object that is being infected.
        :return: 1 if the target node is infected and 0 if the target node is not infected.
        """
        total_infected = len([n for n in node.adjancent_nodes if self.get_node(n).state == 1])
        if self.q <= total_infected / len(node.adjancent_nodes):
            node.pending_state = 1
            return 1
        return 0

    def spread(self):
        still_spreading = True
        time = 0
        time_table = [(time, set(self.starting_nodes))]
        while still_spreading:
            current_infection = self.starting_nodes.copy()
            # TODO: only loop through nodes that are adjacent to infected nodes not all nodes
            for node in list(filter(lambda n: n.name not in time_table[-1][1], self.nodes)):
                infected = self.decide(node)
                if infected:
                    current_infection.append(node.name)
            time += 1
            previous_infected = time_table[-1][1].copy()
            # combine previously infected nodes with nodes infected in this time period
            previous_infected.update(current_infection)
            # add the new time to the time table
            time_table.append((time, previous_infected))
            for node in current_infection:
                self.get_node(node).flip_pending_state()
            if time_table[-1][1] == time_table[-2][1]:  # if there is no state change between current and last time
                return time_table[:len(time_table) - 1]  # return the time_table without the two repeating end states










