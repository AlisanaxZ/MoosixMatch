from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import requests
import os
import jsonpickle
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['UPLOAD_FOLDER'] = "uploads"

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if 'files' not in request.files:
        return jsonify({"error": "Không có tệp"}), 400
    file = request.files['files']
    if file.filename == '':
        return jsonify({"error": "Tệp không có tên hoặc không có tệp"}), 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return file_path

@app.route('/get-music', methods=['GET'])
def get_music():
    location = request.args['location']
    
    data = {
        'api_token': 'a590ad1ecee0441fed52578f1f24afae',
        'return': 'apple_music,spotify',
    }
    files = {
        'file': open(location, 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    return result.text
    

if __name__ == '__main__':
    app.run(debug=True)
