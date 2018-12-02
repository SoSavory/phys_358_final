import numpy as np

class Node:
    def __init__(self, x, y):
        self.position = (x,y)
        self.edges = []

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return self.position[0]*10 + self.position[1]

    def __eqpos__(self, pos):
        return self.position == pos

    def distance_to_other(self, pos):
        return np.sqrt( (self.position[1] - pos[1])**2 + (self.position[0] - pos[0])**2 )
