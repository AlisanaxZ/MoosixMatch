from flask import Flask, request, jsonify
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "uploads"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({"error": "Không có tệp"}), 400
    file = request.files['files']
    if file.filename == '':
        return jsonify({"error": "Tệp không có tên hoặc không có tệp"}), 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    print("OK")
    return jsonify({"message": "Ok r nhe", "filename": file.filename}), 200

if __name__ == '__main__':
    app.run(debug=True)