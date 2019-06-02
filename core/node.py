# Class Node

class Node:
    def __init__(self, position, parrent):
        self.position = position
        self.parrent = parrent
    
    def __str__(self):
        return '{' + str(self.position) + ', ' + str(self.parrent) + '}'


class WeightedNode(Node):
    def __init__(self, position, parrent, weight):
        super().__init__(position, parrent)
        self.weight = weight

    def __str__(self):
        return '{' + str(self.position) + ', ' + str(self.parrent) + ', ' + str(self.weight) + '}'

class ANode(WeightedNode):
    def __init__ (self, position, parrent, weight, x, y):
        super().__init__(position, parrent, weight)
        self.x = x
        self.y = y

    def xy(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")