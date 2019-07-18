from .deterministic import DeterministicGraph
import os


def read_graph(path):
    f_in = open(path)
    num_of_nodes = int(f_in.readline().strip())  # total number of nodes
    starting_node_num = int(f_in.readline().strip())  # starting number for node labels
    q_value = float(f_in.readline().strip())  # q-value
    # make initial infect a list and strip white space from each entry
    initial_infected = list(map(lambda s: s.strip(), f_in.readline().strip().split(',')))
    # cast into integer and subtract by starting node number to create indices
    initial_infected = list(map(lambda s: int(s) - starting_node_num, initial_infected))
    # list of all edges
    edges = list(map(lambda s: s.strip(), f_in.readlines()))
    edges = list(map(lambda s: s.split(','), edges))
    # remove white space for each entry of
    edges = list(map(lambda s: list(map(lambda v: int(v.strip()) - starting_node_num, s)), edges))
    return [num_of_nodes, q_value, initial_infected, edges]


def make_adj_matrix(num_nodes, edges):
    # construct a zero matrix with dimensions num_nodes x num_nodes
    adj = [[0 for col in range(num_nodes)] for row in range(num_nodes)]
    for edge in edges:
        adj[edge[0]][edge[1]] = 1  # undirected graph
        adj[edge[1]][edge[0]] = 1  # start node -> end node set to 1 as well as end node -> start node
    return adj


if __name__ == '__main__':
    g = read_graph('../data/dbm_graded_input.txt')
    adj_m = make_adj_matrix(g[0], g[3])
    d = DeterministicGraph(g[1], g[2], adj_m)
    d.initialize_nodes()
    time_table = d.spread()
    previous_set = set()
    for time in time_table:
        print(f't{time[0]}: {list(time[1] - previous_set)}')
        previous_set = time[1].copy()
    print(f't{time_table[-1][0]}: []')
    print(f'Final: {list(time_table[-1][1])}')

