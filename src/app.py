from flask import Flask, request, jsonify
from config import PORT
from file_repository import FileRepository

app = Flask(__name__)

file_repository = FileRepository()

@app.route('/<path:filename>')
def serve_file(filename: str):
    return file_repository.get(filename)

@app.route('/<path:path>', methods=['POST'])
def upload_file(path: str):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_repository.save(file, path)
        return jsonify({'message': 'File successfully uploaded'}), 200

if __name__ == '__main__':
    app.run(port=PORT)
