import traveler
import graph
import node
import simulation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from operator import itemgetter
import argparse                  # allows us to deal with arguments to main()
from argparse import RawTextHelpFormatter
import glob
import imageio
import os
import time

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

def plotit(path_history, step):
    for p in range(0, path_history.size, step):
        x = []
        y = []
        for i in path_history[p]['path']:
            x.append(i['node'].position[1])
            y.append(i['node'].position[0])
        plt.plot(x, y)
        plt.title("Iteration: " + str(p) + ", Time cost: " + str(path_history[p]['time_cost']))
        plt.savefig(str(p) + ".png")
        plt.close()
    filenames = sorted(glob.glob("*.png"))
    images = []
    with imageio.get_writer('path.gif', mode='I', duration=1) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            os.remove(filename)



def main():
    # ghost grid town
    ggt = graph.Graph()

    # Generate the graph and fill it with a grid of nodes
    for i in range(0,20):
        for j in range(0,20):
            ggt.add_node(i,j)

    for i in range(0,20):
        for j in range(0,20):
            if j != 19:
                ggt.add_edge(ggt.nodes[j + (20*i)], ggt.nodes[j+1+(20*i)], np.random.randint(1,10), np.random.randint(1,10), short_light_1, short_light_1)
            if i != 19:
                ggt.add_edge(ggt.nodes[j + (20*i)], ggt.nodes[j+20+(20*i)], np.random.randint(1,10), np.random.randint(1,10), short_light_2, short_light_2)

    # Homer's odyssey
    homer = traveler.Traveler(ggt, ggt.nodes[0], ggt.nodes[-1])
    print("Current node:")
    print(homer.current_node)

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

    start_time = time.time()
    sim = simulation.Simulation(ggt,homer,100000)
    kept_paths, path_histories = sim.go()
    end_time = time.time()

    print("Run Time: " + str(end_time - start_time))



    sorted_paths = sorted(kept_paths, key=itemgetter('time_cost'))

    print("target node")
    print(homer.target_node)

    print("shortest path: ")
    print(sorted_paths[0])

    print("second shortest path")
    print(sorted_paths[1])

    print("matching paths")
    print(sorted_paths[0]['path'] == sorted_paths[1]['path'])

    plotit(np.asarray(kept_paths), 1000)

    print("Iterations Where minimum path length found: ")
    print([ idx for idx, i in enumerate(list(filter(lambda path: path['time_cost'] == sorted_paths[0]['time_cost'], path_histories))) ])






    # steps = 0
    # while homer.current_node != homer.target_node and steps < 100:
    #     homer.decide_move(homer.get_possible_moves())
    #     steps += 1
    #
    #
    #
    # greedy_time = ggt.time
    #
    # # tuples take form (row, column)
    # node_xs = np.zeros(100)
    # node_ys = np.zeros(100)
    # time_costs = np.zeros(360)
    #
    # for idx, n in enumerate(ggt.nodes):
    #     node_xs[idx] = n.position[1]
    #     node_ys[idx] = n.position[0]
    #
    # # print(len(homer.node_history))
    # node_hist_length = len(homer.node_history)
    # h_xs = np.zeros(node_hist_length)
    # h_ys = np.zeros(node_hist_length)
    #
    # for idx, n in enumerate(homer.node_history):
    #     h_xs[idx] = n.position[1]
    #     h_ys[idx] = n.position[0]
    #
    #
    # plt.scatter(node_xs, node_ys, c='black', marker='.')
    # plt.plot(h_xs, h_ys, c='green', marker='o')
    #
    # # for e in enumerate(ggt.nodes)
    #
    # plt.show()


main()
