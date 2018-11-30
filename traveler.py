import graph
from operator import itemgetter

class Traveler:
    def __init__(self, city, current_node, target_node):
        self.city = city
        self.current_node = current_node
        self.target_node = target_node
        self.node_history = [current_node]



    def get_possible_moves(self):
        possible_moves = []
        for edge in self.current_node.edges:
            if edge['traversibility'] > 0:
                possible_moves.append({'node': edge['node'], 'time_cost': edge['time_cost']})

        return possible_moves

    # Uses an algorithm to decide which move to make. If there are none, the traveler will wait where they are (like they are stopped at a stop light), and recursively decide again after waiting
    def decide_move(self, possible_moves):
        if possible_moves:

            # Decision making and algorithm would go here
            # Greedy algorithm example:

            possible_moves = list(filter(lambda move: move['node'].position[0] > self.current_node.position[0] or move['node'].position[1] > self.current_node.position[1], possible_moves))
            print(possible_moves)
            if possible_moves:
                move = sorted(possible_moves, key=itemgetter('time_cost'))[0]

                # move has form { 'node': node_object, time_cost: int }
                self.make_move(move)
            else:
                self.decide_move(possible_moves)

        else:
            frequency_functions = []
            time = self.city.time

            for edge in self.current_node.edges:
                frequency_functions.append(edge['traversibility_function'])

            # time_step = self.__wait__(frequency_functions,time)

            # self.city.update_time(time_step)
            self.city.update_time(1)
            new_possible_moves = self.get_possible_moves()
            self.decide_move(new_possible_moves)


    def make_move(self, move):

        self.current_node = move['node']
        self.node_history.append(move['node'])
        self.city.update_time(move['time_cost'])
        print(self.current_node.position)

    def __wait__(self, edge_traversibility_functions, sim_time):
        sim_time_2 = sim_time
        sum_traversibility = 0

        while sum_traversibility < 1:
            for f in edge_traversibility_functions:

                sum_traversibility += f(sim_time)
                # print(sum_traversibility)
            sim_time_2 += 1


        return sim_time_2 - sim_time
