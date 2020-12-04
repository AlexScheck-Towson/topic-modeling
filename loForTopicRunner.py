'''
This script prints out the first 3 learning objects assigned to topic A in Pass B

simply update the values for passNum and topicNum
'''
import service
from classManager import LearningObject

passNum = 1
topicNum = 4

result = service.load_learning_objects_for_topic(passNum, topicNum)
print(isinstance(result[0], LearningObject))

print('**********************************************')
for i, x in enumerate(result):
	if i < 3:
		print('---------------------')
		print(x.name)
		print('---------------------')
		print(x.description)
		print('**********************************************')