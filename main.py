import globals
import lexical
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

	print(lexical.get_synonyms("美丽", 32))
	print(lexical.get_synonyms("帅", 32))

	sys.exit(app.exec_())
