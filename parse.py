#function parses a basic sentence and brackets a tree based on the attached grammar

import nltk, re, pprint
from nltk import word_tokenize

def parse(text):
	sent=word_tokenize(text)
	grammar=nltk.data.load('file:PSgrammar.cfg')
	rd_parser=nltk.RecursiveDescentParser(grammar)
	for tree in rd_parser.parse(sent):
		print(tree)
