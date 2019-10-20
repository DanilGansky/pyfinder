# Algorithm: BFS

from core.utils import *
from core.node import Node


def bfs(node_position, node_goal, nodes, neighborhoods, visited, node_parrent):
    previous_node = Node(node_position, node_parrent)

    if not isVisited(previous_node, visited):
        visited.append(previous_node)

    if node_position != node_goal:
        for node in nodes:
            if not isVisited(node, visited):
                if not inNeighborhoods(node, neighborhoods):
                    if node_position == node.parrent:
                        neighborhoods.append(node)

        if len(neighborhoods) > 0:
            node_next = neighborhoods[0]
            del neighborhoods[0]

            return bfs(node_next.position, node_goal, nodes, neighborhoods, visited, node_next.parrent)

    return visited

