import numpy as np

class Node:
    def __init__(self, x, y):
        self.position = (x,y)
        self.edges = []

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return self.position
