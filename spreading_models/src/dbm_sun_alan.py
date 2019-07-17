import pprint
from .deterministic import DeterministicGraph


def read_graph(path):
    f_in = open(path)
    num_of_nodes = int(f_in.readline().strip())
    starting_node_num = int(f_in.readline().strip())
    q_value = float(f_in.readline().strip())
    initial_infected = list(map(lambda s: s.strip(), f_in.readline().strip().split(',')))
    initial_infected = list(map(lambda s: int(s) - starting_node_num, initial_infected))
    edges = list(map(lambda s: s.strip(), f_in.readlines()))
    edges = list(map(lambda s: s.split(','), edges))
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
    adj = make_adj_matrix(g[0], g[3])
    d = DeterministicGraph(g[1], g[2], adj)
    d.initialize_nodes()
    for time in d.spread():
        print(f't_{time[0]} = {time[1]}')
        print(f'Number of Infected: {len(time[1])}')

