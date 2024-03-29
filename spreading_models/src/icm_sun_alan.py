from indepdent_cascade import IndependentCascade


def read_independent_graph(path):
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


if __name__ == '__main__':
    g = read_independent_graph('../data/n.txt')
    icm = IndependentCascade(g[1], g[0], g[3])
    for run in [0]:
        cases = []  # stores the data from each run
        for i in range(1000):
            cases.append(len(icm.spread()[-1][1]))  # number of nodes that ended up being infected
            icm.reset()
        average = round(sum(cases) / len(cases), 3)
        print(f'{run} run average: {average:.3f} nodes infected, '
              f'proportion = {round(average / g[0], 3):.3f}')
