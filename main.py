import csv
import json

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
		print("synonyms:" + globals.linesep)
		for row in rows:
			print(synonyms.nearby(''.join(row), 16))
	print("globals.linesep + ================ End Synonyms ================" + globals.linesep)
	
	with open("paragraphs.csv") as paragraphs_file:
		entity_list = json.loads("entity-list.json")
		rows = csv.reader(paragraphs_file)
		for row in rows:
			text = ''.join(row)
			# word seg
			print(globals.linesep + "================ Word Seg ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			print(jiagu.seg(text))
			print("synonyms:" + globals.linesep)
			print(synonyms.seg(text))
			# entity recognition
			print(globals.linesep + "================ Entity Recognition ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			print(jiagu.ner(''.join(row)))
			print("jionlp:" + globals.linesep)
			entity_recognizer = jionlp.ner.LexiconNER(entity_list)
			print(entity_recognizer(text))
			# extract / generate keywords
			print(globals.linesep + "================ Keywords ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			print(jiagu.keywords(text))
			print("synonyms:" + globals.linesep)
			print(synonyms.keywords(text))
			# extract / generate summary
			
			# sentimental analysis
			
	
	# END CSV TEST
	
	# END TEST CODE
	
	sys.exit(app.exec_())
