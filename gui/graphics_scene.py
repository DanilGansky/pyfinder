# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import *
from graphics_node import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, window):
        QGraphicsScene.__init__(self)
        self.window = window
        self.setSceneRect(0, 0, 100, 100)
        self.nodes = []
        self.counter = 0

        self.window.pushButton_2.clicked.connect(lambda: self.deleteNode(self.window.listWidget.currentRow()))

    def mousePressEvent(self, event):
        x = event.scenePos().x() - 25
        y = event.scenePos().y() - 25

        self.addNode(x, y)
       
    def addNode(self, x, y):
        if not self.isLocated(x, y):
            # self.__log_file.write("Created node #" + str(self.counter) + "\n")
            self.window.textEdit.append("Created node #" + str(self.counter))

            node = GraphicsNode(x, y, self.counter, self)
            self.window.listWidget.addItem("Node #" + str(node.getNumber()))
            self.nodes.append(node)
            self.addItem(node)
            self.counter += 1

    def deleteNode(self, index_node):
        if len(self.nodes) > index_node and index_node >= 0:
            self.removeItem(self.nodes[index_node])
            self.removeItem(self.nodes[index_node].number)
            del self.nodes[index_node]
            node_to_remove = self.window.listWidget.takeItem(index_node)
            self.window.listWidget.removeItemWidget(node_to_remove)
            self.window.textEdit.append("Deleted node #" + str(index_node))

    def isLocated(self, x, y):
        for node_in_nodes in self.nodes:
            if (x >= node_in_nodes.x() - 125 and x <= node_in_nodes.x() + 125) and (y >= node_in_nodes.y() - 125 and y <= node_in_nodes.y() + 125):
                return True


        return False
