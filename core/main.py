# Testing

from utils import *
from bfs import *
from dijkstra import *
import sys

def main():
    map = inputDataFromFile(str(sys.argv[1]))
    option = ""

    if len(sys.argv) > 4:
        option = str(sys.argv[4])

    node_start = int(sys.argv[2])
    node_goal = int(sys.argv[3])
    # nodes = getNodes(map)
    nodes = getWeightedNodes(map)
    neighborhoods = []
    visited = []

    data = dijkstra(node_start, node_goal, nodes, neighborhoods, visited, 0, 0, option)
    way = getShortWay(data[0])
    weight = data[1]

    # way = getShortWay(bfs(node_start, node_goal, nodes, neighborhoods, visited, 0, option))

    print('Way: ')

    print(node_start, end = " ")

    for node in reversed(way):
        print(node.position, end = " ")

    print()

    print("Weight: " + str(weight))

if __name__ == "__main__":
    main()
