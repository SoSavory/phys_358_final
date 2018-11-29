import node

class Edge:
    def __init__(self, node1, node2, time_cost, traversible, ):
        self.node1 = node1
        self.node2 = node2
        self.time_cost = time_cost
        self.traversible = traversible
