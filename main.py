import csv

import jiagu
import jionlp
import synonyms
import textrank4zh

import globals
import lexical
import semantic
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

	# ADD TEST CODE
	
	# SIMPLE TEST
	
	# print(lexical.get_synonyms("美丽", 32))
	# print(lexical.get_synonyms("帅", 32))
	
	# END SIMPLE TEST
	
	# CSV TEST
	
	# synonyms
	print(globals.linesep + "================ Synonyms ================" + globals.linesep)
	with open("synonyms.csv") as synonyms_file:
		rows = csv.reader(synonyms_file)
		for row in rows:
			print(synonyms.nearby(''.join(row), 16))
	print("globals.linesep + ================ End Synonyms ================" + globals.linesep)
	
	with open("paragraphs.csv") as paragraphs_file:
		rows = csv.reader(paragraphs_file)
		for row in rows:
			# word seg
			print(globals.linesep + "================ Word Seg ================" + globals.linesep)
			text = ''.join(row)
			print(synonyms.seg(text))
			print(jiagu.seg(text))
			# entity recognition
			print(globals.linesep + "================ Entity Recognition ================" + globals.linesep)
			print(jiagu.ner(''.join(row)))
			
			# extract / generate keywords
			
			# extract / generate summary
			
			# sentimental analysis
			
	
	# END CSV TEST
	
	# END TEST CODE
	
	sys.exit(app.exec_())
