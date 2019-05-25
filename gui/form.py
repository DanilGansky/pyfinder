# Main window

from window import *
from PyQt5 import *
from graphics_scene import *
import sys

class PyFinderWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        window = self

        self.scene = GraphicsScene(window)
        self.graphicsView.setScene(self.scene)


app = QtWidgets.QApplication(sys.argv)
w = PyFinderWindow()
w.show()
app.exec_()

