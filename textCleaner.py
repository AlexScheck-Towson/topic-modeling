'''
This script manages all of the data prep actions
'''
from html.parser import HTMLParser
import re
# NLTK Stop Words
from nltk.corpus import stopwords
# spacy for lemmatization
import spacy
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess

def performClean(desc_data, passed_stop_words):
	# Remove newline characters and html
	data = [remove_newline_chars_and_html(desc) for desc in desc_data]
	# sentences to words
	data_words = list(sent_to_words(data))
	# remove stop words
	data_words_nostops = remove_stopwords(data_words, passed_stop_words)
	# make bigrams
	bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
	bigram_mod = gensim.models.phrases.Phraser(bigram)
	data_words_bigrams = make_bigrams(data_words_nostops, bigram_mod)
	# lemmatize words
	data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
	# Create Dictionary
	id2word = corpora.Dictionary(data_lemmatized)
	# Create Corpus
	corpus = [id2word.doc2bow(text) for text in data_lemmatized]
	return data_lemmatized, id2word, corpus

##### Helper functions #####
"""
        #####
        #####
        #####
        #####
        #####
       #######
        #####
         ###
          #
"""
class HTMLCleanser(HTMLParser):#####	HTMLCleanser class
	def __init__(self):
		super().__init__()
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)
####	end of HTMLCleanser class

def strip_html_tags(html):	
	cleaner = HTMLCleanser()
	cleaner.feed(html)
	return cleaner.get_data()

# param is single string
def remove_newline_chars(desc):
	return re.sub('\s+', ' ', desc)

# param is single of strings
def remove_newline_chars_and_html(desc):
	data = remove_newline_chars(desc)
	# Remove html
	data = strip_html_tags(data)
	return data

def sent_to_words(sentences):
	for sentence in sentences:
		yield(gensim.utils.simple_preprocess(str(sentence), deacc=True)) # deacc=True remove punctuations

def remove_stopwords(texts, passed_stop_words):
	stop_words = stopwords.words('english')
	stop_words.extend(passed_stop_words)
	return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts, bigram_mod):
	return [bigram_mod[doc] for doc in texts]
	
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
	"""https://spacy.io/api/annotation"""
	nlp = spacy.load('en_core_web_sm')
	texts_out = []
	for sent in texts:
		doc = nlp(" ".join(sent))
		texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
	return texts_out