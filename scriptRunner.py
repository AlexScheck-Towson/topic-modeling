import service

stop_words = []
stop_words.extend(['introduce', 'module', 'introduction', 'issue', 'cover', 'overview', 'topic', 'concept', 'materical', 'focus'])
stop_words.extend(['student', 'process', 'give', 'basic', 'information', 'include', 'computer', 'operation', 'lesson', 'state'])
stop_words.extend(['hour', 'base', 'problem', 'build', 'identify', 'presentation', 'common', 'present', 'micromodule', 'discuss'])
stop_words.extend(['teach', 'class', 'learn', 'exercise', 'lecture', 'activity', 'method', 'important', 'apply', 'step'])
stop_words.extend(['create', 'explain', 'environment', 'complete', 'hand', 'review', 'nanomodule', 'unit', 'also'])
stop_words.extend(['technique', 'tool', 'perform', 'principle', 'understand', 'challenge', 'understanding', 'intend', 'topic', 'implement', 'provide', 'application', 'layer'])

alpha = 30
num_topics =13

def main():
	result = service.execute_full_script(num_topics=num_topics, alpha=alpha, stop_words=stop_words)
	print(result)

# END OF MAIN FUNCTION

if __name__ == "__main__":
	main()