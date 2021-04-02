import flask
import json
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/books")
def get_books():
    books = [
        {'id': 0,
         'title': 'A Fire Upon the Deep',
         'author': 'Vernor Vinge',
         'first_sentence': 'The coldsleep itself was dreamless.',
         'year_published': '1992'},
        {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'},
        {'id': 2,
         'title': 'Dhalgren',
         'author': 'Samuel R. Delany',
         'first_sentence': 'to wound the autumnal city.',
         'published': '1975'}
    ]
    return jsonify(books)


@app.route("/fwa", methods=['GET'])
def get_fwa():
    with open('/etc/netify-fwa/netify-fwa.json', 'r') as f:
        fwa_config = json.load(f)

    print(fwa_config)  # ////

    return jsonify(fwa_config)


@app.route('/fwa', methods=['POST'])
def post_fwa():
    req_json = request.get_json()

    print('req_json', req_json)  # ////

    fwa_path = '/etc/netify-fwa/netify-fwa.json'

    with open(fwa_path, 'r') as f:
        fwa_config = json.load(f)

    with open(fwa_path, 'w') as f:
        fwa_config['rules'].append({
            "type": "block",
            "application": "netify.facebook"
        })

        json.dump(fwa_config, f, indent=2)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
