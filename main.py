import sys
import os

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class MainForm(QMainWindow):
	def __init__(self):
		super(MainForm, self).__init__()
		self.load_ui()

	def load_ui(self):
		loader = QUiLoader()
		path = os.path.join(os.path.dirname(__file__), "MainForm.ui")
		ui_file = QFile(path)
		ui_file.open(QFile.ReadOnly)
		loader.load(ui_file, self)
		ui_file.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainForm()
	# w.resize(250, 150)
	# w.move(300, 300)
	w.setWindowTitle('Simple')
	w.show()
	sys.exit(app.exec_())
