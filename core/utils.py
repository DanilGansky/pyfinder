# Functions for finding shortest path

from node import *

def getNodes(map, nodes_index):
    nodes = []

    for index1, i in enumerate(nodes_index):
        for index2, j in enumerate(nodes_index):
            if map[index1][index2] > 0:
                node = Node(j, i)
                nodes.append(node)

    return nodes

def getWeightedNodes(map, nodes_index):
    nodes = []

    for index1, i in enumerate(nodes_index):
        for index2, j in enumerate(nodes_index):
            if map[index1][index2] > 0:
                weight = map[index1][index2]
                node = WeightedNode(j, i, weight)
                nodes.append(node)

    return nodes

def isVisited(node, visited):
    for node_in_visited in visited:
        if node.position == node_in_visited.position: # and node.parrent == node_in_visited.parrent:
          return True

    return False

def inNeighborhoods(node, neighborhoods):
    for node_in_neighborhoods in neighborhoods:
        if node.position == node_in_neighborhoods.position:#  and node.parrent == node_in_neighborhoods.parrent:
            return True

    return False

def getShortWay(visited, goal):
    node_next = visited[-1]
    way = []

    for node in reversed(visited):
        if node_next.parrent == node.position:
            way.append(node_next)
            node_next = node

    if way and goal == way[-1]:
        return way, True
    else:
        return way, False

def inputDataFromFile(file_name):
    matrix_data = open(file_name, 'r')
    matrix = []

    for row in matrix_data:
        matrix.append(list(map(int, row.split(','))))

    return matrix
