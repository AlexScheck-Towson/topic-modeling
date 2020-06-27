import json
from classManager import LearningObject
import textCleaner

def execute_full_script(num_topics, alpha, stop_words):
	from_file = []

	with open('learning-objects.json', encoding='utf8') as data_file:
		from_file = json.load(data_file)

	all_learning_objects = from_file['objects']
	desc_data = []
	
	my_learning_objects = []
	
	for lo in all_learning_objects:
		desc_data.append(lo['name'] + " " + lo['description'])
		my_learning_objects.append(LearningObject(lo['id'], lo['cuid'], lo['name'], textCleaner.remove_newline_chars_and_html(lo['description'])))
	
	data_lemmatized, id2word, corpus = textCleaner.performClean(desc_data=desc_data, passed_stop_words=stop_words)
	
	print(corpus)