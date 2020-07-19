from flask import Flask, request
from flask_jsonpify import jsonify
from flask_cors import CORS, cross_origin
import json
import service
from classManager import Topic

app = Flask(__name__)
CORS(app)

@app.route("/passNums", methods=["GET"])
def getPassNums():
	passNums = service.get_all_pass_numbers()
	return json.dumps(passNums)

@app.route("/clearPasses", methods=["GET"])
def clearPasses():
	result = service.clear_all_passes()
	return json.dumps(result)

@app.route("/execute", methods=["POST"])
def execute():
	data = request.get_json()
	num_topics = int(data['numTopics'])
	alpha = int(data['alpha'])
	stop_words = data['stopWords']
	result = service.execute_full_script(num_topics=num_topics, alpha=alpha, stop_words=stop_words)
	return json.dumps(result)

@app.route("/topics", methods=["POST"])
def getTopicsForPass():
	data = request.get_json()
	pass_num = int(data['passNum'])
	topics = service.load_topics_for_pass(pass_num)
	return json.dumps([t.__dict__ for t in topics])

@app.route("/learning-objects", methods=["POST"])
def getLearningObjectsForTopic():
	data = request.get_json()
	pass_num = int(data['passNum'])
	topic_num = int(data['topicNum'])
	learning_objects = service.load_learning_objects_for_topic(pass_num, topic_num)
	return json.dumps([lo.__dict__ for lo in learning_objects])

if __name__ == '__main__':
	app.run(port=5002)
