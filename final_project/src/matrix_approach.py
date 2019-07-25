import numpy as np
import random
import heapq


# generate adjacency matrix
def generate_adjacency_matrix(edge_list):
    adj_mat = np.zeros((1000, 1000))
    for edge in edge_list:
        adj_mat[edge[0]][edge[1]] = edge[2]
    return adj_mat


def generate_mat_pow_sum(mat):
    mat_sum = np.zeros((1000, 1000)) + mat
    pow_mat = mat
    for i in range(100):
        pow_mat = np.dot(pow_mat, mat)
        mat_sum += pow_mat
    return list(sum(row for row in mat_sum))


# returns a generated Node object list in which each node has its own children
def generate_node_list(edge_list):
    adj_mat = generate_adjacency_matrix(edge_list)
    node_list = []
    # instantiate nodes
    for node_num in range(1000):
        node_list.append(Node(node_num))
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
    with open(file_name) as file:  # open file and store contents in inFile
        for line in file:
            if line.count('\n') > 0:
                # strip '\n' off
                return_list.append(line[:-1])
            else:
                return_list.append(line)
    return return_list


def quick_run(node_list, seeds):
    all_nodes = node_list.copy()
    for node in all_nodes:
        node.heal()
    for seed_num in seeds:
        all_nodes[seed_num].infect()
    count_sum = 0
    for node in all_nodes:
        if node.infected:
            count_sum += 1
    return count_sum


def katz(adj_mat, c, b):
    return np.dot(np.linalg.inv(np.identity(1000) - adj_mat*c)*b, np.ones(1000))


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


# process read-in file and store in an array
inFile = process_file('../data/new_graph1.txt')
directed_edge_list = process_edges(inFile)
linked_node_list = generate_node_list(directed_edge_list)
adjacency_matrix = generate_adjacency_matrix(directed_edge_list)
# node_mat_vals = generate_mat_pow_sum(adjacency_matrix)
# deg_centrality = list(sum(row for row in adjacency_matrix))
val, vec = np.linalg.eig(adjacency_matrix)
# vec = vec.T
eig_centrality = -1*vec[:, list(val).index(val.max())]
katz_centrality = katz(adjacency_matrix, 0.5, 0.5)
# print(eig_centrality)

# sel_katz = list(list(katz_centrality).index(lbl)
#                   for lbl in heapq.nlargest(20, katz_centrality))
#
# sel_eig = list(list(eig_centrality).index(lbl)
#                   for lbl in heapq.nlargest(35, eig_centrality))
#
# sel_eig.sort()
# sel_katz.sort()

# print(sel_eig)
# print(sel_katz)


# selected_seeds = []
# for elem in sel_katz:
#     # if elem in sel_eig:
#     selected_seeds.append(elem)
#
# print(selected_seeds)
#
# count = 0
# for i in range(1000):
#     count += quick_run(linked_node_list, selected_seeds)
# print(count/1000)


# # demonstrate
# count = []
# for i in range(1000):
#     print(i)
#     a = 0
#     for j in range(50):
#         a += quick_run(linked_node_list, [i])
#     count.append(a/50)
#
# count.sort()
# print(sum(count[-20:]) / )

trials = []
for i in range(1000):
    trials.append(quick_run(linked_node_list, [random.randint(1, 998)
                                               for v in range(20)]))
print(sum(trials) / len(trials))