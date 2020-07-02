import json
from classManager import LearningObject
import textCleaner
import model
import fileUtil

def determine_sentence_topics(ldamodel, corpus, learning_obj_list):	
	for i, topic_list in enumerate(ldamodel[corpus]):
		# sort the list of topics for the individual document by percentage
		# first in list is dominant topic for document
		sorted_topic_list = sorted(topic_list, key=lambda x: (x[1]), reverse=True)
		for j, (topic_num, prop_topic) in enumerate(sorted_topic_list):
			if j == 0: # --> dominant topic
				learning_obj_list[i].primary_topic_num = topic_num
			elif j == 1: # --> 2nd most domminant topic
				learning_obj_list[i].secondary_topic_num = topic_num
			else:
				break;
	return learning_obj_list

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
	
	pass_num = fileUtil.get_next_pass_num()
	fileUtil.create_pass_dir(pass_num)
	
	lda_model = model.run_model_and_save(pass_num=pass_num, corpus=corpus, id2word=id2word, num_topics=num_topics, alpha=alpha)
	my_learning_objects = determine_sentence_topics(ldamodel=lda_model, corpus=corpus, learning_obj_list=my_learning_objects)
	topics_list = model.get_topics_list(lda_model)
	fileUtil.save_all_topics(pass_num=pass_num, topics_list=topics_list)
	
	