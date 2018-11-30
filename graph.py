import node

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.time  = 0

    def add_node(self, x, y):
        new_node = node.Node(x,y)
        self.nodes.append(new_node)

    def add_edge(self, node1, node2, time_cost1, time_cost2, traversibility1, traversibility2, traversibility_function1, traversibility_function2):
        node1.edges.append({"node": node2, "time_cost": time_cost1, "traversibility": traversibility1, "traversibility_function": traversibility_function1})
        node2.edges.append({"node": node1, "time_cost": time_cost2, "traversibility": traversibility2, "traversibility_function": traversibility_function2})

    def update_time(self, time_step):
        self.time += time_step

        for node in self.nodes:
            for edge in node.edges:
                edge['traversibility'] = edge['traversibility_function'](self.time)

    def get_node_from_pos(self, pos):
        for index, node in enumerate(self.nodes):
            if node.__eqpos__(pos):
                return node
