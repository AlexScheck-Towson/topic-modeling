import model
import re
import os
from os import path
james = "files/Pass1/alex.txt"
if path.exists(james):
	os.remove(james)
	print('removed')