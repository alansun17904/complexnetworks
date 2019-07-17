from node import Node


class DeterministicGraph:
    """
    Models the determinisitc model of a node.
    """
    def __init__(self, q, starting_nodes, adj_matrix):
        """

        :param q: The minimum percentage of adjacent nodes for the current node to be infected.
        :param starting_nodes:
        :param adj_matrix:
        """
        self.q = q
        self.starting_nodes = starting_nodes
        self.adj = adj_matrix
        self.nodes = []

    def initialize_nodes(self):
        """

        :return:
        """
        for rindex, row in enumerate(self.adj):
            adj_nodes = [adj_index for adj_index, value in enumerate(self.adj[rindex]) if value == 1]
            state = 1 if rindex in self.starting_nodes else 0
            self.nodes.append(Node(rindex, state, adj_nodes))
        return 1

    def filter_node(self, node_name):
        """
        Returns the node object given the node_name in the graph.
        :param node_name: The name of the node.
        :return: Node object.
        """
        return list(filter(lambda n: n.name == node_name, self.nodes))[0]

    def decide(self, node):
        """

        :param node: A node object that is being infected.
        :return: 1 if the target node is infected and 0 if the target node is not infected.
        """
        total_infected = len([n for n in node.adjancent_nodes if self.filter_node(n).state == 1])
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
            for node in list(filter(lambda n: n.name not in time_table[-1][1], self.nodes)):
                infected = self.decide(node)
                if infected:
                    current_infection.append(node.name)
            time += 1
            previous_infected = time_table[-1][1].copy()
            # combine previously infected nodes with nodes infected in this time period
            previous_infected.update(current_infection)
            time_table.append((time, previous_infected))
            for node in self.nodes:
                node.flip_pending_state()
            if time_table[-1][1] == time_table[-2][1]:  # if there is no state change between current and last time
                return time_table[:len(time_table) - 1]










