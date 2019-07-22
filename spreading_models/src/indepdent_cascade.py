from graph import Graph


class IndependentCascade(Graph):
    def __init__(self, starting_nodes, num_nodes, edge_tuple_with_prob):
        """
        :param starting_nodes: list of the indices of nodes that are initially infected
        :param num_nodes: the number of nodes in the graph
        :param edge_tuple_with_prob: list of Tuple or List that follows the following structure
        (start node index, end node index, edge infection probability)
        """
        self.edge_prob = edge_tuple_with_prob
        super(IndependentCascade, self).__init__(num_nodes, edge_tuple_with_prob, directed=False)
        self.starting_nodes = starting_nodes
        for node in self.nodes.values():
            if node.name in self.starting_nodes:
                node.state = 1

    def _initialize_edges(self):
        super()._initialize_edges()
        for edge in self.edges:
            if self.directed:
                for prob in self.edge_prob:
                    if prob[0] == edge.node1 and prob[1] == edge.node2:
                        edge.q = prob[2]
            else:
                for prob in self.edge_prob:
                    # add the probability weighting to each edge object if the start and end nodes
                    # are same as the edge object
                    if prob[0] == edge.node1.name and prob[1] == edge.node2.name or \
                       prob[1] == edge.node1.name and prob[0] == edge.node2.name:
                        edge.q = prob[2]

    def get_edge(self, node1, node2=None):
        """
        :param node1: (int) Index of the node
        :param node2: (int) Index of the node
        :return: Edge object
        """
        if self.directed and node2 is None:
            raise RuntimeError("Need to give both node1 and node2 to search for edge in directed graph.")
        elif self.directed:
            for edge in self.edges:
                # for directed graphs order of the start and end nodes matter
                if edge.node1 == node1 and edge.node2 == node2:
                    return edge
        else:
            for edge in self.edges:
                # check if the end points of the edges match the end points of the edge object
                if edge.node1 == node1 and edge.node2 == node2 or edge.node1 == node2 and edge.node2 == node1:
                    return edge

    def decide(self, node):
        """
        Decides if a node gets infected or not based on the probability of the adjacent edges.
        :param node: Node object, the node that is being calculated
        :return: 1 if the target node is infected and 0 if the target node is not infected
        """
        adj_nodes = [self.nodes[adj] for adj in node.adjancent_nodes]
        # check if all adjacent nodes are not infected
        infected_adjacent = [n for n in adj_nodes if n.state == 1]
        infected_edges = []
        for adj_node in adj_nodes:
            e = self.get_edge(node, adj_node)
            if (e.node1.state == 1 or e.node2.state == 1) and not e.cant_use:
                infected_edges.append(e)
        # if all adjacent nodes are infected and the node itself is infected it is redundant
        # to check if other nodes are still able to infect those nodes
        for edge in infected_edges:
            if edge.flip_coin():
                for edge in infected_edges:
                    edge.cant_use = True
                # set node's pending state so that it can be changed in the next time
                node.pending_state = 1
                return 1
            else:
                edge.cant_use = True
        return 0

    def spread(self):
        """
        :param t: Number of time periods the program will run before terminating
        :return: Time table in the form of a list of lists in the following structure:
        """
        time = 0
        still_spreading = True
        time_table = [(time, set(self.starting_nodes))]
        while still_spreading:
            # terminating conditions:
            # all edges are used
            current_infection = []
            for node in [n for n in self.nodes.values() if n.state != 1]:
                if self.decide(node):
                    current_infection.append(node.name)
            time += 1
            # combine previously infected nodes with nodes infected in this time period
            previous_infected = time_table[-1][1].copy()
            previous_infected.update(current_infection)
            time_table.append((time, previous_infected))
            for node in current_infection:
                self.nodes[node].flip_pending_state()
            if time_table[-1][1] == time_table[-2][1]:  # if there is no state change between current and last time
                return time_table[:len(time_table) - 1]  # return the time_table without the two repeating end states
        return time_table

    def reset(self):
        """
        Reset all nodes to starting state by setting the states of all nodes except for the starting nodes back
        to 1. Set all the state of the edges back to `can use`.
        :return: None
        """
        for node in self.nodes.values():
            if node.name not in self.starting_nodes:
                node.state = 0
            else:
                node.state = 1
        for edge in self.edges:
            edge.cant_use = False


# TODO: make edges searchable by a special key in dictionary
# TODO: change the edges list into dict data structure
