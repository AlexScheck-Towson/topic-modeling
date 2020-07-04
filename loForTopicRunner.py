import service

result = service.load_learning_objects_for_topic(1, 4)

print('**********************************************')
for i, x in enumerate(result):
	if i < 3:
		print(x)
		print('**********************************************')