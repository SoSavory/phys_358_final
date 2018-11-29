import graph

class Traveller:
    def __init__(self, city, current_node, target_node):
        self.city = city
        self.city_current_node_index, self.current_node = self.city.get_node_from_pos(current_node)
        self.city_target_node_index, self.target_node = self.city.get_node_from_pos(target_node)

    def get_possible_moves(self):
        edges = self.city.nodes[self.city_current_node_index].edges
        possible_end_nodes = []
        for edge in edges:
            if edge['traversibility'] == 1:
                possible_end_nodes.append({'node': edge['node'], time_cost: edge['time_cost']})

        return possible_end_nodes

    def decide_move():

    def make_move():

    def wait(self, edge_traversability_functions):
