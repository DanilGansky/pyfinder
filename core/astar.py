# Algorithm: A*

from utils import *
from node import *
from math import *

def getLengthToGoal(node_goal, node_current):
    return (sqrt(pow((node_goal.x - node_current.x), 2) + pow((node_goal.y - node_current.y), 2))) / 100

def astar(node_position, node_goal, nodes, neighborhoods, visited, node_parrent, weight, x, y):
    previous_node = ANode(node_position, node_parrent, weight, x, y)

    if not isVisited(previous_node, visited):
        visited.append(previous_node)

    if node_position != node_goal.position:
        for node in nodes:
            if not isVisited(node, visited):
                if not inNeighborhoods(node, neighborhoods):
                    if node_position == node.parrent:
                        node.weight = node.weight + weight + getLengthToGoal(node_goal, node)
                        neighborhoods.append(node)

        index_min = 0

        if len(neighborhoods) > 0:
            node_min = neighborhoods[0]

            for index, node in enumerate(neighborhoods):
                if node.weight < node_min.weight:
                    node_min = node
                    index_min = index

            node_next = node_min
            weight = node_next.weight
            x = node_next.x
            y = node_next.y

            del neighborhoods[index_min]

            return astar(node_next.position, node_goal, nodes, neighborhoods, visited, node_next.parrent, weight, x, y)

    return visited, weight