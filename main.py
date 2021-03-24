import sys
import os

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader


class MainForm(QMainWindow):
	def __init__(self):
		super(MainForm, self).__init__()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	UIFileLoader = QUiLoader()
	MainGUI = UIFileLoader.load("MainForm.ui");
	MainGUI.show()
	sys.exit(app.exec_())
