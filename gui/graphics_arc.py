# Graphics arc

from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsTextItem
from PyQt5.QtGui import QPen, QColor

class Arc(QGraphicsLineItem):
    def __init__(self, first_node, second_node, weight, scene):
        QGraphicsLineItem.__init__(self)

        pen = QPen(QColor("green"), 5)
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight
        self.setZValue(1)
        self.setPen(pen)
        self.setLine(self.first_node.x() + 25, self.first_node.y() + 25, self.second_node.x() + 25, self.second_node.y() + 25)

        self.number = QGraphicsTextItem(str(weight))
        self.number.setZValue(6)

        x = (first_node.x() + second_node.x()) / 2
        y = (first_node.y() + second_node.y()) / 2

        self.number.setPos(x, y)

        scene.addItem(self)
        scene.addItem(self.number)
