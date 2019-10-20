# Algorithm: Dijkstra

from core.utils import *
from core.node import WeightedNode


def dijkstra(node_position, node_goal, nodes, neighborhoods, visited, node_parrent, weight):
    previous_node = WeightedNode(node_position, node_parrent, weight)

    if not isVisited(previous_node, visited):
        visited.append(previous_node)

    if node_position != node_goal:
        for node in nodes:
            if not isVisited(node, visited):
                if not inNeighborhoods(node, neighborhoods):
                    if node_position == node.parrent:
                        node.weight += weight
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

            del neighborhoods[index_min]

            return dijkstra(node_next.position, node_goal, nodes, neighborhoods, visited, node_next.parrent, weight)

    return visited, weight
