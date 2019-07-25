import oop_icm
import numpy as np
import random
import logging


def greedy(node_list, linked_node_list):
    """
    :param node_list: list of nodes that are being considered for optimization
    :return: a list of most optimal starting nodes
    """
    finding_max = True
    maximum_initial = []
    while finding_max:
        local_max = []
        avaliable_nodes = set(node_list) - set(maximum_initial)
        for node in avaliable_nodes:
            # number of times icm is to be run
            node_benefit = icm_wrapper(maximum_initial + [node], linked_node_list, .1, 5)
            # logging.debug((maximum_initial + [node], node_benefit))
            local_max.append((node, node_benefit))
        local_max.sort(key=lambda n: n[1])
        maximum_initial.append(local_max[-1][0])
        if len(maximum_initial) == 20:  # the maximum number of nodes that can be infected initially
            return maximum_initial, icm_wrapper(maximum_initial, linked_node_list, 0.1, 1000)


def icm_wrapper(initial_nodes, linked_node_list, min_dev, min_iter):
    count = 0
    std = 0
    run_log = []
    while count < min_iter or std > min_dev:
        run_log.append(oop_icm.quick_run(linked_node_list, initial_nodes))
        if count >= min_iter:
            run_log.sort()
            std = np.std(run_log[1:len(run_log)-1])
        count += 1
    return sum(run_log[1:len(run_log) - 1]) / (len(run_log) - 2)


def deeptop20outdegree(adj_matrix, num, beta):
    outdegree = [(index, sum(v) + beta) for index, v in enumerate(adj_matrix)]
    adj_matrix = adj_matrix.copy()
    for row in range(len(adj_matrix)):
        for col in range(row):
            if adj_matrix[row][col] != 0:
                adj_matrix[row][col] = outdegree[col][1] * (adj_matrix[row][col] + beta)
    deepout = [(index, sum(v)) for index, v in enumerate(adj_matrix)]
    deepout.sort(key=lambda n: n[1])
    return deepout[-num:]


def deeptop20outdegree_ordered(adj_matrix):
    pass


def shallowtop20outdegree(adj_matrix, num):
    outdegree = [(index, sum(v)) for index, v in enumerate(adj_matrix)]
    outdegree.sort(key=lambda n: n[1])
    return outdegree[-num:]


def matrix_power(adj_matrix, num, pow):
    matrixpow = []
    top = np.zeros(len(adj_matrix))
    for i in range(50):
        matrixpow.append(np.linalg.matrix_power(adj_matrix, i))
    for i in range(50):
        toprow = []
        for index, matrix in enumerate(matrixpow):
            toprow.append(sum(matrixpow[i][index]))



if __name__ == '__main__':
    logging.basicConfig(filename='../logging/results.log', level=logging.DEBUG,
                        format='<%(asctime)s>: %(message)s')

    # print(greedy(1000, '../data/new_graph1.txt'))
    edges = oop_icm.process_edges(oop_icm.process_file('../data/cnngnbea.txt'))
    linked_node_list = oop_icm.generate_node_list(edges, 1000)
    adj = oop_icm.generate_adjacency_matrix(edges, 1000)
    t_20 = deeptop20outdegree(adj, 35, 0.4)

    logging.info(greedy([v[0] for v in t_20], linked_node_list))

    # print(icm_wrapper([v[0] for v in t_20], linked_node_list, 0.1, 1000))


