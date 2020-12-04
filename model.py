'''
This script manages the actions performed with the topic modeling algorithm
and the model that it creates
'''
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.utils import SaveLoad
from gensim.models import CoherenceModel

import os
from os import path
from classManager import Topic

# Mallet
currentDir = os.getcwd()
parentDir = os.path.dirname(currentDir)
os.environ['MALLET_HOME'] = path.join(parentDir, 'mallet-2.0.8')
mallet_path = path.join(parentDir, 'mallet-2.0.8', 'bin', 'mallet')

def get_model_path(pass_num):
	return path.join(currentDir, 'files', 'Pass' + str(pass_num),  'malletModel')

def run_model(corpus, id2word, num_topics=13, alpha=30):
	lda_model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word, alpha=alpha)
	return lda_model
	
def run_model_and_save(pass_num, corpus, id2word, num_topics=13, alpha=30):
	lda_model = run_model(corpus, id2word, num_topics, alpha)
	lda_model.save(get_model_path(pass_num))
	return lda_model

def get_coherence(lda_model, data_lemmatized, id2word):
	coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
	return coherence_model_lda.get_coherence()
	
def load_model(pass_num):
	return gensim.utils.SaveLoad.load(get_model_path(pass_num))
	
def get_topics_list(lda_model):
	my_topics = []
	for i, (topic_num, words_list) in enumerate(lda_model.show_topics(num_topics=-1, formatted=False)):
		topic_words = ", ".join([word for word, prop in words_list])
		my_topics.append(Topic(topic_num, topic_words))
	return my_topics
