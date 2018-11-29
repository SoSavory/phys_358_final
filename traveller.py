import graph

class Traveller:
    def __init__(self, city, current_node, target_node):
        self.city = city
        self.city_current_node_index, self.current_node = self.city.get_node_from_pos(current_node)
        self.city_target_node_index, self.target_node = self.city.get_node_from_pos(target_node)



    def get_possible_moves(self):
        possible_moves = []
        for edge in self.current_node.edges:
            if edge['traversibility'] == 1:
                possible_moves.append({'node': edge['node'], time_cost: edge['time_cost']})

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

            # move has form { 'node': node_object, time_cose: int }
            self.make_move(move)


    def make_move(self, move):
        # Need to rethink structures


    def __wait__(self, edge_traversibility_functions, sim_time):
        sim_time_2 = sim_time
        sum_traversibility = 0

        while sum_traversibility < 1:
            for f in edge_traversibility_functions:
                sum_traversibility += f(sim_time)
            sim_time_2 += 1

        return sim_time_2 - sim_time
