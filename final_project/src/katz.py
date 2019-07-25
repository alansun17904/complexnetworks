import numpy as  np
import icm


def create_adj(nodes, edge_list):
    adj = np.zeros((nodes, nodes))
    for edge in edge_list:
        adj[edge[0]][edge[1]] = edge[2]


def katz_centrality(nodes, edge_list):
    pass


if __name__ == '__main__':
    icm.process_file('../data/test1.txt')