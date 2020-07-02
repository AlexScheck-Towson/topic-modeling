import model
import re
import os

files = [f for f in os.listdir('files') if re.match(r'Pass[0-9]+', f)]
max_pass_num = 0
for p in files:
	pass_num = int(p[4::])
	if pass_num > max_pass_num:
		max_pass_num = pass_num

next_pass_num = max_pass_num + 1
print(next_pass_num)

print("creating directory")

try:
	os.mkdir("files/Pass" + str(next_pass_num))
except OSError:
	print("can't make directory")
else:
	print("directory created")