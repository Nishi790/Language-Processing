import nltk
from nltk.corpus import brown

fd=nltk.FreqDist(brown.words(categories='news'))
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#get most frequent words
most_freq_words=fd.most_common(200)

#for each word in most_freq_word tuples, create a dict entry of (word, most common tag)
likely_tags=dict((word,cfd[word].max()) for (word, _) in most_freq_words)

#create tagger that checks the likely_tags dictionary to give tags, then provides 'NN' if none
baseline_tagger=nltk.UnigramTagger(model=likely_tags,
                                   backoff=nltk.DefaultTagger('NN'))

#get set of tagged sentences
brown_tagged_sents=brown.tagged_sents(categories='news')

#print how accurately the tagger tagged the set of tagged sentences
print(baseline_tagger.evaluate(brown_tagged_sents))
