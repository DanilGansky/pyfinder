# Graphics Circle

from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem
from PyQt5.QtGui import QColor, QPen

class Ellipse(QGraphicsEllipseItem):
    def __init__(self, node, weight, scene):
        QGraphicsEllipseItem.__init__(self)

        self.node = node
        self.first_node = node
        self.second_node = node
        self.weight = weight
        pen = QPen(QColor("green"), 5)
        self.setPen(pen)
        self.setZValue(1)
        self.setRect(self.node.x() + 25, self.node.y() + 25, 50, 50)

        self.number = QGraphicsTextItem(str(weight))
        self.number.setZValue(6)

        x = self.node.x()
        y = self.node.y() + 60

        self.number.setPos(x, y)

        scene.addItem(self)
        scene.addItem(self.number)

    def __str__(self):
        return "{" + str(self.node.getNumber()) + ", " + str(self.node.getNumber()) + ", " + str(self.weight) + "}"
