import traveler
import graph
import node
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def always_traversible(t):
    return 1

def never_traversible(t):
    return 0

# Go off-on-off-on
def short_light_1(t):
    return (-1)**t

# go on-off-on
def short_light_2(t):
    return 2 + (-1)**t


def main():
    # ghost grid town
    ggt = graph.Graph()

    possible_functions = [short_light_1, short_light_2]

    # Generate the graph and fill it with a grid of nodes
    for i in range(0,10):
        for j in range(0,10):
            ggt.add_node(i,j)

    for i in range(0,9):
        for j in range(0,10):
            if j != 9:
                ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+1+(10*i)], np.random.randint(10), np.random.randint(10), 0, 0, short_light_1, short_light_1)
                ggt.add_edge(ggt.nodes[j + (10*i)], ggt.nodes[j+10+(10*i)], np.random.randint(10), np.random.randint(10), 1, 1, short_light_2, short_light_2)



main()
