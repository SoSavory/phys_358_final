import traveler
import graph
import node
import numpy as np

class Simulation:
    def __init__(self, city, traveler, iterations):
        self.city = city
        self.traveler = traveler
        self.max_iterations = iterations

        self.deviation_index = 0

        self.current_iterations = 0
        self.current_run_current_time = 0

        # path has form {path: [node_object, node_object, wait (an integer), node, wait, node...], time_cost: int}
        self.path_histories = []

        self.kept_paths = []



    # Returns the node at which the 'greedy-like' algorithm will ignore its previously accepted move for a given node
    # traveler_path is a list of moves like: [{node: node_object, time_cost: int}, int]
    def generate_deviation(self, traveler_path):
        deviation_index = np.random.randint(1,len(traveler_path)-1)
        deviation_node = traveler_path[deviation_index]['node']

        return deviation_index, deviation_node

    # Accepts a path dictionary that is {path: [list of moves], time_cost: int}
    # Allows skipping of performing algorithm, and 'teleports' to deviating node
    def jump_path(self, path):
        self.traveler.current_node = path['path'][-1]['node']
        self.city.time = path['time_cost']


    # Reconstructs a partial path
    def sim_run_path_until(self, path, end_index):
        time = 0
        traveler_path = []
        # time = sum(move['time_cost'] for move in path['path'][0:end_index])
        for i in range(0,end_index):
            time += path['path'][i]['time_cost']
            traveler_path.append(path['path'][i])
        # traveler_path = path['path'][0:end_index]

        return {'path': traveler_path, 'time_cost': time}

    # Accepts a path dictionary that is {path: [list of moves], time_cost: int}
    # moves are {node: node, time_cost: time_cost} or int = time_cost
    # returns a new path dictionary
    # Used to make decisions for a partial path
    def continue_path(self, path, ignored=[]):
        first_move = True
        self.traveler.path = path['path']
        self.jump_path(path)

        while(self.traveler.current_node != self.traveler.target_node):
            possible_moves = self.traveler.get_possible_moves()
            if first_move:
                # print("possible moves")
                # print(possible_moves)
                # print("ignored")
                # print(ignored)
                # print("chosen")

                move = self.traveler.decide_move(possible_moves, ignored)
                # print(move)
                first_move = False
            else:
                move = self.traveler.decide_move(possible_moves)

            self.traveler.make_move(move)
        return {'path': self.traveler.path, 'time_cost': self.city.time}


    def go(self):
        # Generate first path
        self.traveler.path.append({'node': self.traveler.current_node, 'time_cost': 0})
        while self.traveler.current_node != self.traveler.target_node:

            move = self.traveler.decide_move(self.traveler.get_possible_moves())
            self.traveler.make_move(move)

        path_0 = {'path': self.traveler.path, 'time_cost': self.city.time}
        self.path_histories.append(path_0)
        print("initial path")
        print(path_0)

        path_1 = {'path': [], 'time_cost': 0}
        alpha = 1
        for i in range(1, self.max_iterations):
            dev_index, dev_node = self.generate_deviation(path_0['path'])

            partial_path = self.sim_run_path_until(path_0, dev_index)

            path_1 = self.continue_path(partial_path, [dev_node])
            self.path_histories.append(path_1)
            r = path_0['time_cost'] - path_1['time_cost']

            # if r > 1 use new solution
            #
            # Simulated annealing where t = iteration number

            a = np.exp(r/alpha)
            alpha = alpha*0.9
            if a >= np.random.rand():
                path_0 = path_1

            self.kept_paths.append(path_0)

        return self.kept_paths, self.path_histories
