import re
import os
from os import path
import json

def get_next_pass_num():
	files = [f for f in os.listdir('files') if re.match(r'Pass[0-9]+', f)]
	max_pass_num = 0
	for p in files:
		pass_num = int(p[4::])
		if pass_num > max_pass_num:
			max_pass_num = pass_num
	
	return max_pass_num + 1
	
def get_pass_dir_path(pass_num):
	return "files/Pass" + str(pass_num)

def get_topic_file_path(pass_num, topic_num):
	return get_pass_dir_path(pass_num) + "/topic_" + str(topic_num) + ".json"
	
def create_pass_dir(pass_num):
	try:
		os.mkdir("files/Pass" + str(pass_num))
	except OSError:
		print("can't make directory")
	else:
		print("directory created")
		
def save_all_topics(pass_num, topics_list):
	all_topics_path = get_pass_dir_path(pass_num) + "/all_topics.json"
	if path.exists(all_topics_path):
		os.remove(all_topics_path)
	with open(all_topics_path, 'w') as outfile:
		json.dump({'topics': [t.__dict__ for t in topics_list]}, outfile)
		
def save_learning_objects_to_topic(pass_num, topics_list, learning_obj_list):
	for t in topics_list:
		topic_num = t.number
		topic_file_path = get_topic_file_path(pass_num, topic_num)
		los_in_topic = []
		for lo in learning_obj_list:
			if lo.primary_topic_num == topic_num:
				los_in_topic.append(lo)
		with open(topic_file_path, 'w') as outfile:
			json.dump({'learning_objects': [o.__dict__ for o in topics_list]}, outfile)
	