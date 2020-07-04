import re
import os
from os import path
import json
import shutil

def get_next_pass_num():
	pass_dirs = [p for p in os.listdir('files') if re.match(r'Pass[0-9]+', p)]
	max_pass_num = 0
	for d in pass_dirs:
		pass_num = int(d[4::])
		if pass_num > max_pass_num:
			max_pass_num = pass_num
	
	return max_pass_num + 1

def get_all_pass_numbers():
	pass_dirs = [p for p in os.listdir('files') if re.match(r'Pass[0-9]+', p)]
	pass_nums = []
	for d in pass_dirs:
		pass_nums.append(int(d[4::]))
	return pass_nums
	
def get_pass_dir_path(pass_num):
	return path.join("files", "Pass" + str(pass_num))

def get_topic_file_path(pass_num, topic_num):
	return path.join(get_pass_dir_path(pass_num), "topic_" + str(topic_num) + ".json")
	
def create_pass_dir(pass_num):
	try:
		os.mkdir(path.join("files", "Pass" + str(pass_num)))
	except OSError:
		print("can't make directory")
	else:
		print("directory created")
		
def save_all_topics(pass_num, topics_list):
	all_topics_path = path.join(get_pass_dir_path(pass_num), "all_topics.json")
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
			json.dump({'learning_objects': [o.__dict__ for o in los_in_topic]}, outfile)

def clear_all_passes():
	pass_dirs = [p for p in os.listdir('files') if re.match(r'Pass[0-9]+', p)]
	for d in pass_dirs:
		dir_to_remove = path.join("files", d)
		shutil.rmtree(dir_to_remove)

def clear_single_pass(pass_num):
	shutil.rmtree(get_pass_dir_path(pass_num))


def load_topics_for_pass(pass_num):
	path_to_file = path.join(get_pass_dir_path(pass_num), "all_topics.json")
	with open(path_to_file, encoding='utf8') as topics_file:
		from_file = json.load(topics_file)
	return from_file['topics']

def load_learning_objects_for_topic(pass_num, topic_num):
	with open(get_topic_file_path(pass_num, topic_num), encoding='utf8') as lo_file:
		lo_data = json.load(lo_file)
	return lo_data['learning_objects']
