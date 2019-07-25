from typing import List
from random import random


def read_independent_graph(path: str):
    f_in = open(path)
    num_of_nodes = int(f_in.readline().strip())  # total number of nodes
    starting_node_num = int(f_in.readline().strip())  # starting number for node labels
    # make initial infect a list and strip white space from each entry
    initial_infected = list(map(lambda s: s.strip(), f_in.readline().strip().split(',')))
    # cast into integer and subtract by starting node number to create indices
    initial_infected = list(map(lambda s: int(s) - starting_node_num, initial_infected))
    rounds = list(map(lambda s: int(s.strip()), f_in.readline().strip().split(',')))
    # list of all lines for edge entries
    raw_edges = list(map(lambda s: s.strip(), f_in.readlines()))
    # remove white space for each entry of edges and format into int and float data type
    edges = []
    for edge in raw_edges:
        edge_attributes = []
        for index, entry in enumerate(edge.split(',')):
            if index == 2:
                edge_attributes.append(float(entry))
            else:
                edge_attributes.append(int(entry) - starting_node_num)
        edges.append(edge_attributes)
    f_in.close()
    return [num_of_nodes, initial_infected, rounds, edges]


def setup(num_of_nodes: int, initial_infected: List[int], edges: List[List]):
    adj_matrix = [[0 for col in range(num_of_nodes)] for row in range(num_of_nodes)]
    for edge in edges:
        adj_matrix[edge[0]][edge[1]] = edge[2]
        adj_matrix[edge[1]][edge[0]] = edge[2]
    return adj_matrix, initial_infected, []


def main():
    g = read_independent_graph('../data/n.txt')
    adj, currently_infected, pending_infected = setup(g[0], g[1], g[3])
    for round in g[2]:
        for run in range(round):
            c = currently_infected.copy()
            still_spreading = True
            while still_spreading:
                p = []
                for node in set(list(range(len(adj))).append(c)):
                    for flip in [v for v in adj[node] if v != 0]:
                        if random.random() < flip:
                            p.append(node)
                if len(p) == 0:
                    return c
                else:
                    c.append(p)


if __name__ == '__main__':
    g = read_independent_graph('../data/n.txt')
    print(main())
