'''
This script retrieves and prints the topics for the set passNum
'''
import service
from classManager import Topic

passNum = 1

result = service.load_topics_for_pass(passNum)
print()
print(isinstance(result[0], Topic))
for i, topic in enumerate(result):
	print('---------------------')
	print('Topic ' + str(topic.number))
	print('---------------------')
	print(topic.key_words)
	print('**********************************************')