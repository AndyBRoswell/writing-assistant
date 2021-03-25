import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QObject, Signal, Slot
from Ui_MainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.show()


app = None
gui = None

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = MainWindow()

	sys.exit(app.exec_())
