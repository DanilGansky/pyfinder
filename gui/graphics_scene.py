# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import *
from graphics_node import *
from graphics_arc import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, window):
        QGraphicsScene.__init__(self)
        self.window = window
        self.setSceneRect(0, 0, 100, 100)
        self.nodes = []
        self.counter = 0
        self.buffer = []

        self.window.pushButton_2.clicked.connect(lambda: self.deleteNode(self.window.listWidget.currentRow()))
        self.window.pushButton.clicked.connect(self.connectNodes)

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

    def deleteNode(self, index_node):
        if len(self.nodes) > index_node and index_node >= 0:
            self.removeItem(self.nodes[index_node])
            self.removeItem(self.nodes[index_node].number)
            del self.nodes[index_node]

            node_to_remove = self.window.listWidget.takeItem(index_node)
            self.window.listWidget.removeItemWidget(node_to_remove)

            self.buffer.clear()
            self.window.state.setText("Clear buffer")

            self.window.textEdit.append("Deleted node #" + str(index_node))

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
       arc = Arc(self.buffer[0], self.buffer[1], self.window.spinBox.value(), self)
       self.window.state.setText("Node #" + self.buffer[0].getNumber() + " and node #" + self.buffer[1].getNumber() + " - connected!")
       self.buffer.clear()
