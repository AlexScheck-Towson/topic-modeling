import service
from classManager import Topic

result = service.load_topics_for_pass(1)
print(isinstance(result[0], Topic))