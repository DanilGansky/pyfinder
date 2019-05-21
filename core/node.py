# Class Node

class Node:
    def __init__(self, position, parrent):
        self.position = position
        self.parrent = parrent

    def show(self):
        print(self.position)
        print(self.parrent)


class WeightedNode(Node):
    def __init__(self, position, parrent, weight):
        super().__init__(position, parrent)
        self.weight = weight

    def show(self):
        print('{' + str(self.position) + ', ' + str(self.parrent) + ', ' + str(self.weight) + '}')
