# Class Node

class Node:
    def __init__(self, position, parrent):
        self.position = position
        self.parrent = parrent

    def show(self):
        print(self.position)
        print(self.parrent)
    
    def __str__(self):
        return '{' + str(self.position) + ', ' + str(self.parrent) + '}'


class WeightedNode(Node):
    def __init__(self, position, parrent, weight):
        super().__init__(position, parrent)
        self.weight = weight

    def __str__(self):
        return '{' + str(self.position) + ', ' + str(self.parrent) + ', ' + str(self.weight) + '}'
