import oop_icm
import numpy as np


def greedy(node_list, linked_node_list):
    """
    Greedy algorithm for finding the set of initially infected nodes to maximize spread
    :param node_list: list of nodes that are being considered for optimization
    :return: a tuple of a list of most optimal starting nodes List[int] and a float with the average number
    of nodes infected from this optimized list.
    """
    finding_max = True
    maximum_initial = []
    while finding_max:
        local_max = []  # List[Tuple(int, float)] contribution of each node + nodes from `maximum_initial`
        available_nodes = set(node_list) - set(maximum_initial)  # nodes that are still available for selection
        for node in available_nodes:
            # number of times icm is to be run
            node_benefit = icm_wrapper(maximum_initial + [node], linked_node_list, .5, 10)
            local_max.append((node, node_benefit))
        local_max.sort(key=lambda n: n[1])
        maximum_initial.append(local_max[-1][0])  # get the node that added the largest value
        if len(maximum_initial) == 20:  # the maximum number of nodes that can be infected initially
            return maximum_initial, icm_wrapper(maximum_initial, linked_node_list, 0.1, 100)


def icm_wrapper(initial_nodes, linked_node_list, min_dev, min_iter):
    """
    Wrapper for ICM
    :param initial_nodes: Initial nodes that are infected.
    :param linked_node_list:
    :param min_dev: The minimum standard deviation for the program to stop
    :param min_iter: The minimum amount of iterations the program must run
    :return: The average number of nodes are were infected
    """
    count = 0
    std = 0
    run_log = []
    # continue while the program does not satisfy the minimum number of runs or
    # the standard deviation of the result from each run is above the std_dev threshold.
    while count < min_iter or std > min_dev:
        run_log.append(oop_icm.quick_run(linked_node_list, initial_nodes))
        if count >= min_iter:
            run_log.sort()
            # standard deviation with the maximum and minimum value removed.
            std = np.std(run_log[1:len(run_log)-1])
        count += 1
    # average with the first (min) and last (max) element of the sorted list removed.
    return sum(run_log[1:len(run_log) - 1]) / (len(run_log) - 2)


def degree_katz_centrality(adj_matrix, num, beta):
    """
    :param adj_matrix: Adjacency matrix
    :param num: The number of possible initial starting nodes returned.
    :param beta: (float) dictates the beta value
    :return: a list of indices for possible initial nodes.
    """
    # vector with the out degree of each node
    out_degree = [(index, sum(v) + beta) for index, v in enumerate(adj_matrix)]
    adj_matrix = adj_matrix.copy()
    for row in range(len(adj_matrix)):
        for col in range(row):
            if adj_matrix[row][col] != 0:
                # centrality is the summation of the importance of adjacent nodes
                # multiplied by the probability of infection of that nodes + a beta value
                adj_matrix[row][col] = out_degree[col][1] * (adj_matrix[row][col] + beta)
    # creates a katz centrality vector from the newly formed adjacency matrix
    katz = [(index, sum(v)) for index, v in enumerate(adj_matrix)]
    katz.sort(key=lambda n: n[1])
    return katz[-num:]



def degree_centrality(adj_matrix, num):
    """
    Ranks nodes by the summation of their edge weights
    :param adj_matrix: List[List] adjacency matrix
    :param num: The number of nodes being returned
    :return: List[int], nodes with top eigen weight edges.
    """
    out_degree = [(index, sum(v)) for index, v in enumerate(adj_matrix)]
    out_degree.sort(key=lambda n: n[1])  # sort according to degree centrality
    return out_degree[-num:]


def eig(adj, num):
    """
    Calculates the eigen vector and returns a tuple with the top num eigen values.
    [(v1, e1), (v2, e2), ... , (v_num, e_num)]
    :param adj: Adjacency matrix
    :param num: The number of greatest eigen values returned
    :return: List[int] with length num of the greatest eigen values.
    """
    val, vec = np.linalg.eig(adj)
    eig_central = vec[:, list(val).index(val.max())]  # find the eigen vector for the maximum eigen value
    e = list(enumerate(eig_central))  # create tuple pairs of node index and eigen value
    e.sort(key=lambda n: n[1])  # sort according to eigen value
    return e[-num:]


def pick_seeds(path):
    """
    :param path: Path to input file
    :return: List[int] of optimized initial nodes.
    """
    edges = oop_icm.process_edges(oop_icm.process_file(path))
    linked_node_list = oop_icm.generate_node_list(edges, 1000)
    adj = oop_icm.generate_adjacency_matrix(edges, 1000)
    top = eig(adj, 35)
    return greedy([v[0] for v in top], linked_node_list)[0]

