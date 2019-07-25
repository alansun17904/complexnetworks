import random
import copy


# processes a list of edges and convert them from string to integer
# split the pairs of edges by comma and strips any leading / trailing spaces
def process_edges(edges_string_list):
    adj_list = {}
    for line in edges_string_list:
        pair = line.split(',')
        startnode = int(pair[0])
        endnode = int(pair[1])
        prob = float(pair[2])
        if startnode not in adj_list:
            adj_list[startnode] = [[endnode, prob]]
        else:
            adj_list[startnode].append([endnode, prob])
    return adj_list


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


# read in string of nodes and store in a list
def process_csn(comma_spaced_string):
    return_list = []
    comma_spaced_string = comma_spaced_string.split(',')
    for element in comma_spaced_string:
        return_list.append(int(element.strip()))
    return return_list


# execute each run and returns the number of nodes infected in the end
def run(node_list, edge_list):
    edge_list = edge_list.copy()
    t = 0
    infected_nodes = set(node_list)
    currently_infected = set()
    while len(infected_nodes - currently_infected) != 0:
        previously_infected = infected_nodes.copy() if t == 0 else currently_infected.copy()
        currently_infected = set()
        for node in previously_infected:
            for edge in edge_list[node]:
                if edge[0] not in infected_nodes:
                    if random.random() <= edge[1]:
                        currently_infected.update([edge[0]])
                    edge_list[node].remove(edge)
        infected_nodes.update(currently_infected)
    return len(infected_nodes)


if __name__ == '__main__':
    inFile = process_file('../data/edge_case3.txt')
    edgelist = process_edges(inFile)
    a = [run([1], edgelist) for v in range(100)]
    print(sum(a) / len(a))
