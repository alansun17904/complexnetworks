import numpy as np
import random


def generate_adjacency_matrix(edge_list, n):
    """
    generate adjacency matrix
    :param edge_list:
    :param n:
    :return:
    """
    adjacency_matrix = np.zeros((n, n))
    for edge in edge_list:
        adjacency_matrix[edge[0]][edge[1]] = edge[2]
    return adjacency_matrix


def generate_node_list(edge_list, n):
    """
    :param edge_list: Edge list created from `process_edges` (List[List]) in the format of
    [[v1, v2, p1], [v1, v3, p2], ... [v_n, v_m, p_n]]
    where v_n marks the starting node, v_m marks the end node, and p_n denotes the
    probability of infection spreading from v_n to v_m
    :param n: The number of nodes in the graph
    :return: A list of node objects
    """
    adj_mat = generate_adjacency_matrix(edge_list, n)
    # instantiate nodes
    node_list = [Node(i) for i in range(n)]
    # make connections
    for edge in edge_list:
        node_list[edge[0]].add_child(node_list[edge[1]], adj_mat[edge[0]][edge[1]])
    return node_list


def process_edges(edges_string_list):
    """
    processes a list of edges and convert them from string to integer
    split the pairs of edges by comma and strips any leading / trailing spaces
    :param edges_string_list:
    :return: A list of all the edges List[List]
    [[v1, v2, p1], [v1, v3, p2], ... [v_n, v_m, p_n]]
    """
    edge_list = []
    for line in edges_string_list:
        pair = line.split(',')
        edge_list.append([int(pair[0]), int(pair[1]), float(pair[2])])
    return edge_list


def process_file(file_name):
    """
    Strips whitespace from each line.
    :param file_name: path to file
    :return: A list of all the lines of the file.
    """
    f_in = open(file_name)
    return list(map(lambda s: s.strip(), f_in.readlines()))


def quick_run(node_list, seeds):
    """
    Finds the number of infected nodes using the ICM model.
    :param node_list: List of all node objects in the graph
    :param seeds: List[int] initially infected nodes
    :return: an int denoting the number of nodes infected
    """
    all_nodes = node_list.copy()
    for node in all_nodes:
        node.heal()
    for seed_num in seeds:
        all_nodes[seed_num].infect()
    return sum([1 if node.infected else 0 for node in all_nodes])


class Node(object):
    """
    Represents a node
    """
    def __init__(self, n: int):
        """
        :param n: The index of the node [int]
        """
        self.n = n
        self.child = []
        self.infected = False

    def add_child(self, cd, wt: float):
        """
        Adds the child node and the edge weight connecting the two nodes to a list of child nodes.
        :param cd: Child node (Node object)
        :param wt: (float) the weight of the edge connecting the two nodes
        :return: None
        """
        self.child.append([cd, wt])

    def infect(self):
        """

        :return:
        """
        self.infected = True
        for cd in self.child:
            if not cd[0].infected and random.random() < cd[1]:
                cd[0].infect()

    def heal(self):
        """
        Resets the state of the node to 'not infected'
        :return:
        """
        self.infected = False
