# Graphics Scene

from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import *

class GraphicsScene(QGraphicsScene):
    def __init__(self, parrent = None):
        QGraphicsScene.__init__(self, parrent)
        self.setSceneRect(0, 0, 100, 100)

    def mousePressEvent(self, event):
        pen = QPen(QColor(0, 0, 0))
        brush = QBrush(QColor(50, 50, 50))

        x = event.scenePos().x() - 25
        y = event.scenePos().y() - 25

        self.addRect(x, y, 50, 50, pen, brush)

