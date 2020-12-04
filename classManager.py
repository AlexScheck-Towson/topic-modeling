'''
This script simply holds the LearningObject and Topic classes
'''
class LearningObject:
	def __init__(self, id, cuid, name, description):
		self.id = id
		self.cuid = cuid
		self.name = name
		self.description = description
		self.primary_topic_num = -1
		self.secondary_topic_num = -1

class Topic:
	def __init__(self, number, key_words):
		self.number = number
		self.key_words = key_words
		self.total_lo_num = 0