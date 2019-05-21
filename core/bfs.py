# Algorithm: BFS

from utils import *
from node import *

def bfs(node_position, node_goal, nodes, neighborhoods, visited, node_parrent, option):
    previous_node = Node(node_position, node_parrent)

    if not isVisited(previous_node, visited):
        visited.append(previous_node)

    if node_position != node_goal:
        for node in nodes:
            if not isVisited(node, visited):
                if not inNeighborhoods(node, neighborhoods):
                    if node_position == node.parrent:
                        neighborhoods.append(node)

        if option == "debug":
            print("Nodes: ")

            for node in neighborhoods:
                node.show()

            print('Visited: ')

            for node in neighborhoods:
                node.show()

            print()

        node_next = neighborhoods[0]

        del neighborhoods[0]

        # print(neighborhoods[0].position)
    
        return bfs(node_next.position, node_goal, nodes, neighborhoods, visited, node_next.parrent, option)

    return visited

