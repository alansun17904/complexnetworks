from deterministic import DeterministicGraph
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
    return [num_of_nodes, q_value, initial_infected, edges, starting_node_num]


if __name__ == '__main__':
    g = read_graph('../data/dbm_graded_input.txt')
    d = DeterministicGraph(q=g[1], starting_nodes=g[2], num_nodes=g[0],
                           edge_tuple=g[3])
    time_table = d.spread()
    previous_set = set()
    for time in time_table:
        # add the starting node number back to the indices
        infected_at_t = [node_label + g[4] for node_label in list(time[1] - previous_set)]
        # sort the list so it matches desired output
        infected_at_t.sort()
        print(f't{time[0]}: {infected_at_t}')
        # so does not change the previous comparison time when subtracted
        previous_set = time[1].copy()
    print(f't{time[0] + 1}: []')
    # add starting node to final list
    final = [node_label + g[4] for node_label in list(time[1])]
    final.sort()
    print(f'Final: {final}')

