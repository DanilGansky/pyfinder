# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import *
from graphics_node import *
from graphics_arc import *
import sys

sys.path.append("../core/")

from bfs import *
from dijkstra import *
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
            self.window.state.setText("Ready to connect node #" + str(self.buffer[0].getNumber() + " and node #" + str(self.buffer[1].getNumber())))
        elif data[0] and len(self.buffer) == 2:
            self.buffer.clear()
            self.window.state.setText("Clear buffer. Nodes disconnected")

       
    def addNode(self, x, y):
        if not self.isLocated(x, y):
            # self.__log_file.write("Created node #" + str(self.counter) + "\n")
            self.window.textEdit.append("Created node #" + str(self.counter))

            node = GraphicsNode(x, y, self.counter, self)
            self.window.listWidget.addItem("Node #" + str(node.getNumber()))
            self.nodes.append(node)
            self.addItem(node)
            self.counter += 1

            self.updateListNodes()

    def deleteNode(self, index_node):
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

                        if listItem.text() == "Arc: first node #" + str(arc.first_node.getNumber()) + ", second node #" + str(arc.second_node.getNumber()):
                            index_of_arc = i


                    arc_to_remove = self.window.listWidget_2.takeItem(index_of_arc)
                    self.window.listWidget_2.removeItemWidget(arc_to_remove)

                    self.window.textEdit.append("Deleted arc: first node #" + str(arc.first_node.getNumber()) + ", second node #" + str(arc.second_node.getNumber()))

            del self.nodes[index_node]

            node_to_remove = self.window.listWidget.takeItem(index_node)
            self.window.listWidget.removeItemWidget(node_to_remove)

            self.buffer.clear()
            self.window.state.setText("Clear buffer")

            self.window.textEdit.append("Deleted node #" + str(index_node))

            self.updateListNodes()

    def deleteArc(self, index_arc):
        if len(self.arcs) > index_arc and index_arc >= 0:
            self.removeItem(self.arcs[index_arc])
            self.removeItem(self.arcs[index_arc].number)

            arc_to_remove = self.window.listWidget_2.takeItem(index_arc)
            self.window.listWidget_2.removeItemWidget(arc_to_remove)

            self.buffer.clear()
            self.window.state.setText("Clear buffer")

            self.window.textEdit.append("Deleted arc: first node #" + str(self.arcs[index_arc].first_node.getNumber()) + ", second node #" + str(self.arcs[index_arc].second_node.getNumber()))
            del self.arcs[index_arc]

    def isLocated(self, x, y):
        for node_in_nodes in self.nodes:
            if (x >= node_in_nodes.x() - 125 and x <= node_in_nodes.x() + 125) and (y >= node_in_nodes.y() - 125 and y <= node_in_nodes.y() + 125):
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
        if len(self.buffer) == 2:
            arc = Arc(self.buffer[0], self.buffer[1], self.window.spinBox.value(), self)
            self.arcs.append(arc)
            self.window.listWidget_2.addItem("Arc: first node #" + str(self.buffer[0].getNumber()) + ", second node #" + str(self.buffer[1].getNumber()))

            self.window.state.setText("Node #" + self.buffer[0].getNumber() + " and node #" + self.buffer[1].getNumber() + " - connected!")
            self.window.textEdit.append("Node #" + self.buffer[0].getNumber() + " and node #" + self.buffer[1].getNumber() + " - connected!")
            self.buffer.clear()

    def getArcs(self, node):
        arcs = []

        for arc in self.arcs:
            if arc.first_node == node or arc.second_node == node:
                arcs.append(arc)

        return arcs

    def updateListNodes(self):
        self.window.comboBox.clear()
        self.window.comboBox_2.clear()

        for node in self.nodes:
            self.window.comboBox.addItem("Node #" + str(node.getNumber()))
            self.window.comboBox_2.addItem("Node #" + str(node.getNumber()))

    def generateMatrix(self):
        matrix = []
        matrix_row = []

        for i in range(len(self.nodes)):
            tempArcs = self.getArcs(self.nodes[i])
            arcs = [] 
            matrix_row.clear()

            for arc in tempArcs:
                if int(arc.first_node.getNumber()) != i:
                    arc.reverse()
                    arcs.append(arc)
                else:
                    arcs.append(arc)

            for j in range(len(self.nodes)):
                for arc in arcs:
                    if j == int(arc.second_node.getNumber()):
                        matrix_row.append(arc.weight)

                if len(matrix_row) <= j:
                    matrix_row.append(0)

            matrix.append(list(matrix_row))

        return matrix

    def find(self):
        map = self.generateMatrix()

        node_start = int(self.window.comboBox.currentText().split("#")[1])
        node_goal = int(self.window.comboBox_2.currentText().split("#")[1])
        nodes = getWeightedNodes(map)

        option = "debug"
        visited = []
        neighborhoods = []

        algorithm = self.window.comboBox_3.currentText()

        if algorithm == "BFS":
            way = getShortWay(bfs(node_start, node_goal, nodes, neighborhoods, visited, 0, option))

        print("Way: ")

        print(node_start, end = " ")

        for node in reversed(way):
            print(node.position, end = " ")

        print()


