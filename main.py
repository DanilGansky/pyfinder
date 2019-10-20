from PyQt5.QtWidgets import QApplication
from gui.form import PyFinderWindow
import sys


def main():
	app = QApplication(sys.argv)
	w = PyFinderWindow()
	w.show()
	app.exec_()


if __name__ == '__main__':
	main()