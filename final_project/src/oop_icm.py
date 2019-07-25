import numpy as np
import random


# generate adjacency matrix
def generate_adjacency_matrix(edge_list, n):
    adjacency_matrix = np.zeros((n, n))
    for edge in edge_list:
        adjacency_matrix[edge[0]][edge[1]] = edge[2]
    return adjacency_matrix


# returns a generated Node object list in which each node has its own children
def generate_node_list(edge_list, n):
    adj_mat = generate_adjacency_matrix(edge_list, n)
    # instantiate nodes
    node_list = [Node(i) for i in range(n)]
    # make connections
    for edge in edge_list:
        node_list[edge[0]].add_child(node_list[edge[1]],
                                     adj_mat[edge[0]][edge[1]])
    return node_list


# processes a list of edges and convert them from string to integer
# split the pairs of edges by comma and strips any leading / trailing spaces
def process_edges(edges_string_list):
    return_list = []
    for line in edges_string_list:
        pair = line.split(',')
        return_list.append([int(pair[0]), int(pair[1]), float(pair[2])])
    return return_list


# read, interpret and store contents from a file
def process_file(file_name):
    return_list = []
    f_in = open(file_name)
    return list(map(lambda s: s.strip(), f_in.readlines()))
    # with open(file_name) as file:  # open file and store contents in inFile
    #     for line in file:
    #         if line.count('\n') > 0:
    #             # strip '\n' off
    #             return_list.append(line[:-1])
    #         else:
    #             return_list.append(line)
    # return return_list


def quick_run(node_list, seeds):
    all_nodes = node_list.copy()
    for node in all_nodes:
        node.heal()
    for seed_num in seeds:
        all_nodes[seed_num].infect()
    count_sum = 0
    return sum([1 if node.infected else 0 for node in all_nodes])
    # for node in all_nodes:
    #     if node.infected:
    #         count_sum += 1
    # return count_sum


class Node(object):

    def __init__(self, n):
        self.n = n
        self.child = []
        self.infected = False

    def add_child(self, cd, wt):
        self.child.append([cd, wt])

    def get_index(self):
        return self.n

    def infect(self):
        self.infected = True
        for cd in self.child:
            if not cd[0].infected and random.random() < cd[1]:
                cd[0].infect()

    def heal(self):
        self.infected = False


# # process read-in file and store in an array
# inFile = process_file('../data/new_graph1.txt')
# directed_edge_list = process_edges(inFile)
# linked_node_list = generate_node_list(directed_edge_list)
# trials = [quick_run(linked_node_list, [1]) for v in range(100)]
# print(sum(trials) / len(trials))