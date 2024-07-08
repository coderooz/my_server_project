# app.py

from flask import Flask, send_from_directory
from config import Config

app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
app.config['SERVER_NAME'] = Config.SERVER_NAME

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
