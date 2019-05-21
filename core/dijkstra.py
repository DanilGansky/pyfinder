# Algorithm: Dijkstra

from utils import *
from node import *

def dijkstra(node_position, node_goal, nodes, neighborhoods, visited, node_parrent, weight, option):
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

        if option == "debug":
            print('Nodes:')
    
            for node in neighborhoods:
                node.show()

            # print('Weight: ' + str(weight))

            print('Visited: ')

            for node in visited:
                 node.show()

            print()

        # node_next = neighborhoods[0]

        # del neighborhoods[0]

        index_min = 0

        node_min = neighborhoods[0]

        for index, node in enumerate(neighborhoods):
            if node.weight < node_min.weight:
                node_min = node
                index_min = index

        node_next = node_min
        weight = node_next.weight

        del neighborhoods[index_min]

        """
        node_min.show()
        print("Index: " + str(index_min))

        """

        # print(neighborhoods[0].position)
    
        return dijkstra(node_next.position, node_goal, nodes, neighborhoods, visited, node_next.parrent, weight, option)

    return visited, weight
