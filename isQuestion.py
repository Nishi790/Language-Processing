import nltk,re,pprint
from nltk import word_tokenize

def questionWord(text):
	questionwords=["who","what","where","when","why","how"]
	if text[0].casefold() in questionwords:
		return True
	else:
		return False
		

def verbFollows(words):
	if (words[1][1]=="VBP" or words[1][1]=="VBD"):
		return True
	
def verbInitial(words):
	verbs=["is", "are", "am", "have", "has", "had", "will", "can", "did", "do", "does"]
	if words[0][0].casefold() in verbs:
		return True
	else:
		return False
	

def isQuestion(text):
	temp=word_tokenize(text)
	words=nltk.pos_tag(temp)
	start=questionWord(words[0])
	if start:
		if verbFollows(words):
			return True
		else:
			return False
	elif (words[0][1]=="VBP" or words[0][1]=="VBD"):
		return True
	elif verbInitial(words):
		return True
	else:
		return False
