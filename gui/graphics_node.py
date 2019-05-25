# Node

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsRectItem
from PyQt5.QtGui import QFont, QBrush, QPen, QColor

class GraphicsNode(QGraphicsRectItem):
    def __init__(self, x, y, number, scene):
        QGraphicsRectItem.__init__(self)
        self.setRect(x, y, 50, 50)
        self.setBrush(QBrush(QColor(50, 50, 50)))
        self.setPen(QPen(QColor("black")))
        self.__x = x
        self.__y = y
        
        self.number = QGraphicsTextItem(str(number))
        self.number.setPos(x, y)
        self.number.setZValue(10)
        scene.addItem(self.number)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def getNumber(self):
        return self.number.toPlainText()
