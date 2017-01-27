import re

def splitText(text):
	words=re.split(r'(;|,|\.|\?|!|\s)\s*',text)	
	for word in words:
		if word==(" "):
			words.remove(word)
		elif word==(""):
			words.remove(word)
	return words

def splitSentences(text):
	sentences=re.split(r'[\.|\?|!|;]\s*',text)
	for sentence in sentences:
		if sentence==(""):
			sentences.remove(sentence)
	print (sentences)
	return sentences

def starts(verbs,questionword, sentence):
	if sentence.startswith(questionword):
		words=sentence.split()
		if words[1].casefold() in verbs:
			return True
		else:
			return False
			
def supportQs(verbs,sentence):
	words=splitText(sentence)
	if words[0].casefold() in verbs:
		return True
	else:
		return False

		

		
def isQuestion(verbs,text):
	sentences=splitSentences(text)
	for sentence in sentences:
		a=starts(verbs,"What", sentence)
		b=starts(verbs,"Who", sentence)
		c=starts(verbs,"Where", sentence)
		d=starts(verbs,"When", sentence)
		e=starts(verbs,"Why", sentence)
		f=starts(verbs,"How",sentence)
		g=supportQs(verbs,sentence)
		if a:
			print("\""+sentence+"\" is a question.")
		elif b:
			print("\""+sentence+"\" is a question.")
		elif c:
			print("\""+sentence+"\" is a question.")
		elif d:
			print("\""+sentence+"\" is a question.")
		elif e:
			print("\""+sentence+"\" is a question.")
		elif f:
			print("\""+sentence+"\" is a question.")
		elif g:
			print("\""+sentence+"\" is a question.")
		else:
			print("\""+sentence+"\" is not a question.")

verbs=['is','are','was','were','did','does','do','will','have','has','had']
isQuestion(verbs,"Who are you? What you want is pie. Are you my mother? Do you know my mother?")