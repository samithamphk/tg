# import modules
from flask import Flask
from flask import request
import json
import traffic_guard_model
# api routes


app = Flask(__name__)


@app.route('/tg/score', methods=["POST"])
def similarity_score():
    if request.method == 'POST':
        ip = request.form.get('ip',False)
        score = traffic_guard_model.get_similarity_score(ip)
        res = {'ip': ip, 'score': score}
        return json.dumps(res)

@app.route('/tg/test', methods=["GET"])
def index():
    if request.method == 'GET':
        return "Traffic Guard Test: Hello From Sahas"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')