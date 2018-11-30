import graph

class Traveler:
    def __init__(self, city, current_node, target_node):
        self.city = city
        self.current_node = current_node
        self.target_node = target_node



    def get_possible_moves(self):
        possible_moves = []
        for edge in self.current_node.edges:
            if edge['traversibility'] > 0:
                possible_moves.append({'node': edge['node'], 'time_cost': edge['time_cost']})

        return possible_moves

    def decide_move(self, possible_moves):
        if not possible_moves:
            frequency_functions = []
            time = self.city.time

            for edge in self.current_node.edges:
                frequency_functions.append(edge['traversibility_function'])

            time_step = self.__wait__(frequency_functions,time)
            self.city.update_time(time_step)
            new_possible_moves = self.get_possible_moves()
            self.decide_move(new_possible_moves)
        else:
            # Decision making and algorithm would go here

            # move has form { 'node': node_object, time_cost: int }
            self.make_move(move)


    def make_move(self, move):
        self.current_node = move['node']
        self.city.update_time(move['time_cost'])


    def __wait__(self, edge_traversibility_functions, sim_time):
        sim_time_2 = sim_time
        sum_traversibility = 0

        while sum_traversibility < 1:
            for f in edge_traversibility_functions:
                sum_traversibility += f(sim_time)
            sim_time_2 += 1

        return sim_time_2 - sim_time
