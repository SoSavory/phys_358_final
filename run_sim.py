import traveler
import graph
import node
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Traversibility/stop-light functions

def always_traversible(t):
    return 1

def never_traversible(t):
    return 0

# Go off-on-off-on
def short_light_1(t):
    return (-1)**(t+1)

# go on-off-on
def short_light_2(t):
    return 1 + (-1)**t


def main():
    # ghost grid town
    ggt = graph.Graph()

    # Generate the graph and fill it with a grid of nodes
    for i in range(0,10):
        for j in range(0,10):
            ggt.add_node(i,j)

    for i in range(0,9):
        for j in range(0,10):
            if j != 9:
                ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+1+(10*i)], np.random.randint(10), np.random.randint(10), 0, 0, short_light_1, short_light_1)
            ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+10+(10*i)], np.random.randint(10), np.random.randint(10), 1, 1, short_light_2, short_light_2)

    # Homer's odyssey
    homer = traveler.Traveler(ggt, ggt.nodes[0], ggt.nodes[-1])


    # print(ggt.nodes[-1].edges)
    # print(ggt.get_node_from_pos((2,2)))
    print(homer.get_possible_moves()[0]['node'].position)
    # print(ggt.nodes[10].edges)

    ggt.update_time(1)

    print(homer.get_possible_moves()[0]['node'].position)
    # print(ggt.nodes[10].edges)


main()
