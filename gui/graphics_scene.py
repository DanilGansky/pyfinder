# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPen, QColor, QBrush
from graphics_node import *
from graphics_arc import *
import sys

sys.path.append("../core")

from bfs import *
from dijkstra import *
from astar import *
from utils import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, window):
        QGraphicsScene.__init__(self)

        self.window = window
        self.setSceneRect(0, 0, 100, 100)
        self.nodes = []
        self.arcs = []
        self.counter = 0
        self.buffer = []
        self.matrix = []
        self.matrixXY = []

        self.window.pushButton_2.clicked.connect(lambda: self.deleteNode(self.window.listWidget.currentRow()))
        self.window.pushButton_3.clicked.connect(lambda: self.deleteArc(self.window.listWidget_2.currentRow()))
        self.window.pushButton.clicked.connect(self.connectNodes)
        self.window.pushButton_4.clicked.connect(self.find)

    def mouseReleaseEvent(self, event):
        x = event.scenePos().x() - 25
        y = event.scenePos().y() - 25

        self.addNode(x, y)

    def mouseDoubleClickEvent(self, event):
        x = event.scenePos().x()
        y = event.scenePos().y()

        data = self.isNode(x, y)

        if data[0] and len(self.buffer) == 0:
            self.buffer.append(data[1])
            self.window.state.setText("Buffer contain node #" + data[1].getNumber())
        elif data[0] and len(self.buffer) == 1:
            self.buffer.append(data[1])
            self.window.state.setText(\
                "Ready to connect node #" + str(self.buffer[0].getNumber()\
                + " and node #" + str(self.buffer[1].getNumber())))
        elif data[0] and len(self.buffer) == 2:
            self.buffer.clear()
            self.window.state.setText("Clear buffer. Nodes disconnected")

    def addNode(self, x, y):
        self.cleanArcs()

        if not self.isLocated(x, y):
            node = GraphicsNode(x, y, self.counter, self)
            self.window.listWidget.addItem("Node #" + str(node.getNumber()))
            self.nodes.append(node)
            self.addItem(node)
            self.counter += 1

            self.updateListNodes()

    def deleteNode(self, index_node):
        self.cleanArcs()

        if len(self.nodes) > index_node and index_node >= 0:
            self.removeItem(self.nodes[index_node])
            self.removeItem(self.nodes[index_node].number)

            arcs_to_remove = self.getArcs(self.nodes[index_node])

            if len(arcs_to_remove) > 0:
                for arc in arcs_to_remove:
                    self.removeItem(arc)
                    self.removeItem(arc.number)
                    self.arcs.remove(arc)

                    index_of_arc = 0

                    for i in range(self.window.listWidget_2.count()):
                        listItem = self.window.listWidget_2.item(i)

                        if listItem.text() == "Arc: {" + str(arc.first_node.getNumber())\
                            + ", " + str(arc.second_node.getNumber())\
                            + ", " + str(arc.weight) + "}":
                            index_of_arc = i


                    arc_to_remove = self.window.listWidget_2.takeItem(index_of_arc)
                    self.window.listWidget_2.removeItemWidget(arc_to_remove)

            del self.nodes[index_node]

            node_to_remove = self.window.listWidget.takeItem(index_node)
            self.window.listWidget.removeItemWidget(node_to_remove)

            self.buffer.clear()
            self.window.state.setText("Clear buffer")

            self.updateListNodes()

    def deleteArc(self, index_arc):
        self.cleanArcs()

        if len(self.arcs) > index_arc and index_arc >= 0:
            self.removeItem(self.arcs[index_arc])
            self.removeItem(self.arcs[index_arc].number)

            arc_to_remove = self.window.listWidget_2.takeItem(index_arc)
            self.window.listWidget_2.removeItemWidget(arc_to_remove)

            self.buffer.clear()
            self.window.state.setText("Clear buffer")

            del self.arcs[index_arc]

    def isLocated(self, x, y):
        for node_in_nodes in self.nodes:
            if (x >= node_in_nodes.x() - 125 and x <= node_in_nodes.x() + 125)\
                and (y >= node_in_nodes.y() - 125 and y <= node_in_nodes.y() + 125):
                return True

        return False

    def isNode(self, x, y):
        data_to_return = []

        for node_in_nodes in self.nodes:
            if (x >= node_in_nodes.x() and x <= node_in_nodes.x() + 50) and (y >= node_in_nodes.y() and y <= node_in_nodes.y() + 50):
                data_to_return.append(True)
                data_to_return.append(node_in_nodes)

                return data_to_return

        data_to_return.append(False)

        return data_to_return

    def connectNodes(self):
        self.cleanArcs()

        if len(self.buffer) == 2:
            if not self.isArc():
                if self.buffer[0] != self.buffer[1]:
                    arc = Arc(self.buffer[0], self.buffer[1], self.window.spinBox.value(), self)

                    self.arcs.append(arc)
                    self.window.listWidget_2.addItem(\
                        "Arc: {" + str(self.buffer[0].getNumber())\
                        + ", " + str(self.buffer[1].getNumber())\
                        + ", " + str(self.window.spinBox.value()) + "}"\
                    )

                    self.window.state.setText(\
                        "Node #" + self.buffer[0].getNumber()\
                        + " and node #" + self.buffer[1].getNumber()\
                        + " - connected!")
                    self.buffer.clear()

    def getArcs(self, node):
        arcs = []

        for arc in self.arcs:
            if arc.first_node == node or arc.second_node == node:
                arcs.append(arc)

        return arcs

    def isArc(self):
        for arc_in_arcs in self.arcs:
            if (self.buffer[0] == arc_in_arcs.first_node and self.buffer[1] == arc_in_arcs.second_node)\
                or (self.buffer[1] == arc_in_arcs.first_node and self.buffer[0] == arc_in_arcs.second_node):
                    return True

        return False

    def getArc(self, first_node, second_node):
        for arc in self.arcs:
            if (first_node == int(arc.first_node.getNumber()) and second_node == int(arc.second_node.getNumber())) \
                or (second_node == int(arc.first_node.getNumber()) and first_node == int(arc.second_node.getNumber())):
                    return arc

    def getNodeById(self, node_index):
        for node in self.nodes:
            if int(node.getNumber()) == node_index:
                return node

    def getANodeById(self, node_goal, nodes):
        for node in nodes:
            if node.position == node_goal:
                return node

        return ANode(node_goal, node_goal, 0, 0, 0)

    def updateListNodes(self):
        self.window.comboBox.clear()
        self.window.comboBox_2.clear()

        for node in self.nodes:
            self.window.comboBox.addItem("Node #" + str(node.getNumber()))
            self.window.comboBox_2.addItem("Node #" + str(node.getNumber()))

    def generateMatrix(self):
        self.matrix.clear()
        self.matrixXY.clear()
        matrix_row = []
        matrix_row_XY = []
        xy = []
        status = False

        for node in self.nodes:
            i = int(node.getNumber())
            tempArcs = self.getArcs(node)
            arcs = []
            matrix_row.clear()
            matrix_row_XY.clear()

            for arc in tempArcs:
                if int(arc.first_node.getNumber()) != i:
                    arc.reverse()
                    arcs.append(arc)
                else:
                    arcs.append(arc)

            for nodeColumn in self.nodes:
                j = int(nodeColumn.getNumber())
                xy.clear()
                status = False

                for arc in arcs:
                    if j == int(arc.second_node.getNumber()):
                        matrix_row.append(arc.weight)

                        xy.append(arc.second_node.x())
                        xy.append(arc.second_node.y())
                        matrix_row_XY.append(xy)

                        status = True

                if status == False:
                    matrix_row.append(0)

                    xy.append(0)
                    xy.append(0)
                    matrix_row_XY.append(xy)

            self.matrix.append(list(matrix_row))
            self.matrixXY.append(list(matrix_row_XY))

    def find(self):
        if len(self.nodes) > 0:
            self.generateMatrix()
            map = list(self.matrix)
            mapXY = list(self.matrixXY)

            """
            for row in mapXY:
                for column in row:
                    print(column, end = "\t")
                print()
            """

            node_start = int(self.window.comboBox.currentText().split("#")[1])
            node_goal = int(self.window.comboBox_2.currentText().split("#")[1])
            nodes_index = []

            for node in self.nodes:
                nodes_index.append(int(node.getNumber()))

            nodes = getNodes(map, nodes_index, mapXY)

            visited = []
            neighborhoods = []
            algorithm = self.window.comboBox_3.currentText()
            way = []
            weight = 0
            result = False

            node_xy = self.getNodeById(node_start)
            anode_goal = self.getANodeById(node_goal, nodes)
            x = node_xy.x()
            y = node_xy.y()

            # anode_goal.xy()

            if algorithm == "BFS":
                way_and_result = getWay(bfs(node_start, node_goal, nodes, neighborhoods, visited, 0), node_goal)
                way = way_and_result[0]
                result = way_and_result[1]
            elif algorithm == "Dijkstra":
                way_data = dijkstra(node_start, node_goal, nodes, neighborhoods, visited, 0, 0)
                way_and_result = getWay(way_data[0], node_goal)
                way = way_and_result[0]
                result = way_and_result[1]
                weight = way_data[1]
            elif algorithm == "A*":
                way_data = astar(node_start, anode_goal, nodes, neighborhoods, visited, 0, 0, x, y)
                way_and_result = getWay(way_data[0], node_goal)
                way = way_and_result[0]
                result = way_and_result[1]
                weight = way_data[1]

            if result:
                self.showWay(way, weight)

    def cleanArcs(self):
        for arc in self.arcs:
            arc.setPen(QPen(QColor("green"), 5))

    def showWay(self, way, weight):
        self.cleanArcs()

        for i in range(len(way)):
            arc = self.getArc(way[i].position, way[i].parrent)

            if arc:
                arc.setPen(QPen(QColor("pink"), 5))

        if weight > 0:
            self.window.state.setText("Weight: " + str(weight))
