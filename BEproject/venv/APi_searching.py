from flask import Flask, request
from json import dumps
from LOGIC_searching import sort_a_list_of_lines
from flask_cors import CORS
from threading import Thread

app = Flask(__name__)
CORS(app)


@app.route("/post", methods=['POST'])
def post():
    data = request.get_json()
    return dumps(sort_a_list_of_lines(data.get('pathWordsFile'), data.get('pathDirectory')))


if __name__ == '__main__':
    Thread(target=app.run).start()
