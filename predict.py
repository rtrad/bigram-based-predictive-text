import nltk
from nltk.collocations import *
from random import randint

print 'Enter model corpus file name:'
filename = raw_input()
f = open(filename)
rawtext = f.read()


word1 = input('Starting word: ')
sentence = word1
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()



tokens = nltk.word_tokenize(rawtext)

finder = BigramCollocationFinder.from_words(tokens)
#finder.apply_freq_filter(3)
finder.apply_ngram_filter(lambda w1, w2: word1 != w1)

word2 = finder.nbest(bigram_measures.likelihood_ratio, 5)[randint(0,len(finder.nbest(bigram_measures.likelihood_ratio, 5))-1)][1]
#print finder.nbest(bigram_measures.likelihood_ratio, 10)
sentence += ' ' + word2

for i in range(1, 200):
	finder = TrigramCollocationFinder.from_words(tokens)
	finder.apply_freq_filter(3)
	finder.apply_ngram_filter(lambda w1, w2, w3: word1 != w1 or word2 != w2)
	if len(finder.nbest(trigram_measures.likelihood_ratio, 5)) < 1:
		finder = BigramCollocationFinder.from_words(tokens)
		finder.apply_ngram_filter(lambda w1, w2: word2 != w1)
		word1 = word2
		word2 = finder.nbest(bigram_measures.likelihood_ratio, 5)[randint(0,len(finder.nbest(bigram_measures.likelihood_ratio, 5))-1)][1]
		#print finder.nbest(bigram_measures.likelihood_ratio, 10)
		#print 'bigram needed'
	else:
		word1 = word2
		word2 = finder.nbest(trigram_measures.likelihood_ratio, 5)[randint(0,len(finder.nbest(trigram_measures.likelihood_ratio, 5))-1)][2]
		#print finder.nbest(trigram_measures.likelihood_ratio, 10)
	sentence += ' ' + word2

print sentence