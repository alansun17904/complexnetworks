import icm
import numpy as np


def greedy(num_of_nodes):
    """
    :param num_of_nodes: the number of nodes in the optimimization problem
    :return: a list of most optimal starting nodes
    """
    edges = icm.process_edges(icm.process_file('../data/edge_case3.txt'))
    finding_max = True
    maximum_initial = []
    while finding_max:
        local_max = []
        avaliable_nodes = set(range(num_of_nodes)) - set(maximum_initial)
        for node in avaliable_nodes:
            # number of times icm is to be run
            node_benefit = icm_wrapper(maximum_initial + [node], edges, 1, 10)
            local_max.append(node_benefit)
        local_max.append(list(avaliable_nodes)[list(local_max).index(max(local_max))])
        if len(maximum_initial) == 2:  # the maximum number of nodes that can be infected initially
            return list(map(lambda n: n + 1, maximum_initial))


def icm_wrapper(initial_nodes, edges, min_dev, min_iter):
    count = 0
    std = 0
    run_log = []
    while count < min_iter or std > min_dev:
        run_log.append(icm.run(initial_nodes, edges))
        if count >= min_iter:
            run_log.sort()
            std = np.std(run_log[1:len(run_log)-1])
        count += 1
    return sum(run_log[1:len(run_log) - 1]) / (len(run_log) - 2)


if __name__ == '__main__':
    print(greedy(15))

