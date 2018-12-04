import graph
from operator import itemgetter

class Traveler:
    def __init__(self, city, current_node, target_node):
        self.city = city
        self.current_node = current_node
        self.target_node = target_node

        # path is of form [{node: node_object, time_cost: int}, int = wait, etc...]
        self.path = []

        # This stores a node and its distance from the target node
        # has form {node_object: distance}
        self.node_distances_from_target = {current_node: self.current_node.distance_to_other(self.target_node.position)}


    # ignored is a list of nodes to not include in the possible moves
    def get_possible_moves(self):
        possible_moves = []
        for edge in self.current_node.edges:
            if edge['traversibility_function'](self.city.time) > 0:
                possible_moves.append({'node': edge['node'], 'time_cost': edge['time_cost']})

        return possible_moves

    # Uses an algorithm to decide which move to make.
    def decide_move(self, possible_moves, ignored=[]):

        possible_moves = list(filter(lambda move: move['node'] not in ignored, possible_moves))

        # We only calculate the distance of a node to the objective when it is needed, and only one time.
        for move in possible_moves:
            if (move['node'] not in self.node_distances_from_target):
                self.node_distances_from_target[move['node']] = move['node'].distance_to_other(self.target_node.position)

        move = sorted(possible_moves, key=self.__vel_sort__)[-1]

        return move


    # if move is an int, it represents a wait for the duration = move. Otherwise move is a node and a time to wait
    def make_move(self, move):
        if type(move) is not int:
            self.current_node = move['node']
            # Take a look at this. The simulated partial paths might be way over thought!!!
            self.city.update_time(move['time_cost'])
        else:
            self.city.update_time(move)

        self.path.append(move)

    # The greedy algorith wants to get as close as possible as fast as possible
    def __vel_sort__(self, move):
        return (self.node_distances_from_target[self.current_node] - self.node_distances_from_target[move['node']])/move['time_cost']
