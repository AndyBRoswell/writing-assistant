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
	print(globals.linesep + "================ End Synonyms ================" + globals.linesep)
	
	print(globals.linesep + "================ Lexical & Semantic ================" + globals.linesep)
	with open("paragraphs.csv") as paragraphs_file, open("entity-list.json", encoding = "utf-8") as entity_list_file:
		entity_list = json.load(entity_list_file)
		jio_entity_recognizer = jionlp.ner.LexiconNER(entity_list)
		tr4w = textrank4zh.TextRank4Keyword()
		tr4s = textrank4zh.TextRank4Sentence()
		rows = csv.reader(paragraphs_file)
		for row in rows:
			text = ''.join(row)
			print("text: " + globals.linesep + text)
			
			# word seg
			print(globals.linesep + "================ Word Seg ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			words = jiagu.seg(text)
			print(words)
			print("synonyms:" + globals.linesep)
			print(synonyms.seg(text))
			
			# entity recognition
			print(globals.linesep + "================ Entity Recognition ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			print(jiagu.ner(words))
			print("jionlp:" + globals.linesep)

			print(jio_entity_recognizer(text))
			
			# extract / generate keywords
			print(globals.linesep + "================ Keywords ================" + globals.linesep)
			keyword_count = 16
			print("jiagu:" + globals.linesep)
			print(jiagu.keywords(text, keyword_count))
			print("synonyms:" + globals.linesep)
			print(synonyms.keywords(text, keyword_count))
			print("textrank4zh:" + globals.linesep)
			tr4w.analyze(text = text)
			tr4w_keywords = tr4w.get_keywords(keyword_count)
			for word_item in tr4w_keywords:
				print(word_item.word)
			
			# extract / generate summary
			print(globals.linesep + "================ Summaries ================" + globals.linesep)
			print("jiagu:" + globals.linesep)
			print(jiagu.summarize(text, 3))
			print("jionlp:" + globals.linesep)
			print(jionlp.summary.extract_summary(text))
			print("textrank4zh:" + globals.linesep)
			tr4s.analyze(text)
			tr4s_summaries = tr4s.get_key_sentences()
			for sentence_item in tr4s_summaries:
				print(sentence_item.sentence)
			
			# sentimental analysis
			print("jiagu:" + globals.linesep)
			print(jiagu.sentiment(text))
			print("jionlp:" + globals.linesep)
			jio_sentiment_analyzer = jionlp.sentiment.LexiconSentiment()
			print(jio_sentiment_analyzer(text))
	
	print(globals.linesep + "================ End Lexical & Semantic ================" + globals.linesep)
	
	# END CSV TEST
	
	# END TEST CODE
	
	sys.exit(app.exec_())
