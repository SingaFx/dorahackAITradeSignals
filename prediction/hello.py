import scraper
from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getstuff')
def hello_world():
    return jsonify(scraper.startUp())