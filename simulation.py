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



    # Returns the node at which the 'greedy-like' algorithm will ignore its previously accepted move for a given node
    # traveler_path is a list of moves like: [{node: node_object, time_cost: int}, int]
    def generate_deviation(self, traveler_path):
        steps = self.__remove_ints_from_list__(traveler_path)
        stripped_path_index = np.random.randint(1,len(steps)-1)
        node = steps[stripped_path_index+1]['node']
        # print("NODE")
        # print(node)
        absolute_index = 0
        for i in range(0, len(traveler_path)):
            if type(traveler_path[i]) is not int:
                if traveler_path[i]['node'].__eq__(node):
                    absolute_index = i - 1
                    break

        return absolute_index, node

    def __remove_ints_from_list__(self, tlist):
        return list(filter(lambda item: type(item) is not int, tlist))

    def __remove_non_ints_from_list__(self, tlist):
        return list(filter(lambda item: type(item) is int, tlist))

    # Accepts a path dictionary that is {path: [list of moves], time_cost: int}
    # Allows skipping of performing algorithm, and 'teleports' to deviating node
    def jump_path(self, path):
        self.traveler.current_node = path['path'][-1]['node']
        self.city.time = path['time_cost']

    # Reconstructs a partial path
    def sim_run_path_until(self, path, end_index):
        traveler_path = []
        time = 0
        # print("End index: " + str(end_index))
        for move in path['path'][0:end_index+1]:
            if type(move) is not int:
                time += move['time_cost']
            else:
                time += move
            traveler_path.append(move)
        # print({'path': traveler_path, 'time_cost': time})
        return {'path': traveler_path, 'time_cost': time}

    # Accepts a path dictionary that is {path: [list of moves], time_cost: int}
    # moves are {node: node, time_cost: time_cost} or int = time_cost
    # returns a new path dictionary
    # Used to make decisions for a partial path
    def continue_path(self, path, ignored=[]):
        print("continue path:")
        print(path)
        print("ignored:")
        print(ignored)
        first_move = True
        self.traveler.path = path['path']
        # print("=====================================")
        # print(self.traveler.current_node.position)
        # print(self.city.time)
        # print("=====================================")
        self.jump_path(path)
        # print(self.traveler.current_node.position)
        # print(self.city.time)
        # print("=====================================")
        # print("continuing a path")
        # print(ignored)

        # print(self.traveler.current_node)
        while(self.traveler.current_node != self.traveler.target_node):
            possible_moves = self.traveler.get_possible_moves()

            if first_move:
                move = self.traveler.decide_move(possible_moves, ignored)
                first_move = False
            else:
                move = self.traveler.decide_move(possible_moves)

            self.traveler.make_move(move)
        return {'path': self.traveler.path, 'time_cost': self.city.time}


    def go(self):
        # Generate first path

        while self.traveler.current_node != self.traveler.target_node:
            # print(self.traveler.current_node.position)
            # print(self.traveler.node_distances_from_target)

            move = self.traveler.decide_move(self.traveler.get_possible_moves())
            self.traveler.make_move(move)

        print(self.traveler.path)

        path_0 = {'path': self.traveler.path, 'time_cost': self.city.time}
        self.path_histories.append(path_0)

        path_1 = {'path': [], 'time_cost': 0}
        alpha = 1
        for i in range(1, self.max_iterations):
            print("iteration" + str(i))
            dev_index, dev_node = self.generate_deviation(path_0['path'])
            # print(dev_node)
            partial_path = self.sim_run_path_until(path_0, dev_index)
            # possible_moves = self.traveler.get_possible_moves(ignored=[dev_node])
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

        return self.path_histories
