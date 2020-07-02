import re
import os

def get_next_pass_num():
	files = [f for f in os.listdir('files') if re.match(r'Pass[0-9]+', f)]
	max_pass_num = 0
	for p in files:
		pass_num = int(p[4::])
		if pass_num > max_pass_num:
			max_pass_num = pass_num
	
	return max_pass_num + 1
	
def get_pass_dir_path(pass_num):
	return "files/Pass" + int(pass_num)
	
def create_pass_dir(pass_num):
	try:
		os.mkdir("files/Pass" + str(pass_num))
	except OSError:
		print("can't make directory")
	else:
		print("directory created")