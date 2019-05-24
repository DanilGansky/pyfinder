# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import *
from graphics_node import *

class GraphicsScene(QGraphicsScene):
    def __init__(self):
        QGraphicsScene.__init__(self)
        self.setSceneRect(0, 0, 100, 100)
        self.nodes = []
        self.counter = 0

    def mousePressEvent(self, event):
        x = event.scenePos().x() - 25
        y = event.scenePos().y() - 25

        self.addNode(x, y)
       
    def addNode(self, x, y):
        if not self.isLocated(x, y):
            node = GraphicsNode(x, y, self.counter, self)
            self.nodes.append(node)
            self.addItem(node)
            self.counter += 1

    def isLocated(self, x, y):
        for node_in_nodes in self.nodes:
            if (x >= node_in_nodes.x() - 125 and x <= node_in_nodes.x() + 125) and (y >= node_in_nodes.y() - 125 and y <= node_in_nodes.y() + 125):
                return True


        return False
