import traveler
import graph
import node
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse                  # allows us to deal with arguments to main()
from argparse import RawTextHelpFormatter

# Traversibility/stop-light functions

def always_traversible(t):
    return 1

def never_traversible(t):
    return 0

# Go off-on-off-on
def short_light_1(t):
    if t % 2 != 0:
        return 1
    else:
        return 0

# go on-off-on
def short_light_2(t):
    if t % 2 == 0:
        return 1
    else:
        return 0


def main():
    # ghost grid town
    ggt = graph.Graph()

    # Generate the graph and fill it with a grid of nodes
    for i in range(0,10):
        for j in range(0,10):
            ggt.add_node(i,j)

    for i in range(0,10):
        for j in range(0,10):
            if j != 9:
                ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+1+(10*i)], np.random.randint(10), np.random.randint(10), short_light_1, short_light_1)
            if i != 9:
                ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+10+(10*i)], np.random.randint(10), np.random.randint(10), short_light_2, short_light_2)

    # Homer's odyssey
    homer = traveler.Traveler(ggt, ggt.nodes[0], ggt.nodes[-1])


    # print(ggt.nodes[-1].edges)
    # print(ggt.get_node_from_pos((2,2)))
    # print(homer.get_possible_moves()[0]['node'].position)
    # # print(ggt.nodes[10].edges)
    #
    # ggt.update_time(1)
    #
    # print(homer.get_possible_moves()[0]['node'].position)
    # print(ggt.nodes[10].edges)


    edge_count = 0
    for node in ggt.nodes:
        for edge in node.edges:
            edge_count += 1

    print(edge_count)

    steps = 0
    while homer.current_node != homer.target_node and steps < 100:
        homer.decide_move(homer.get_possible_moves())
        steps += 1

    print(homer.current_node.position)
    print(ggt.time)
    # tuples take form (row, column)
    node_xs = np.zeros(100)
    node_ys = np.zeros(100)
    time_costs = np.zeros(360)

    for idx, n in enumerate(ggt.nodes):
        node_xs[idx] = n.position[1]
        node_ys[idx] = n.position[0]

    # print(len(homer.node_history))
    node_hist_length = len(homer.node_history)
    h_xs = np.zeros(node_hist_length)
    h_ys = np.zeros(node_hist_length)

    for idx, n in enumerate(homer.node_history):
        h_xs[idx] = n.position[1]
        h_ys[idx] = n.position[0]






    plt.scatter(node_xs, node_ys, c='black', marker='.')
    plt.plot(h_xs, h_ys, c='green', marker='o')
    plt.show()


main()
