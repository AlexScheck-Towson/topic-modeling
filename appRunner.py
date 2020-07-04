from flask import Flask, request
from flask_jsonpify import jsonify
from flask_cors import CORS, cross_origin
import json
import service
from classManager import Topic

app = Flask(__name__)
CORS(app)

@app.route("/topics", methods=["POST"])
def getTopicsForPass():
	data = request.get_json()
	pass_num = int(data['passNum'])
	topics = service.load_topics_for_pass(pass_num)
	return json.dumps([ob.__dict__ for ob in topics])



if __name__ == '__main__':
	app.run(port=5002)
