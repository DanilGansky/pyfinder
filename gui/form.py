# Main window

from gui.window import Ui_Form
from PyQt5.QtWidgets import QWidget
from gui.graphics_scene import GraphicsScene


class PyFinderWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        window = self

        self.scene = GraphicsScene(window)
        self.graphicsView.setScene(self.scene)
