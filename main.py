#!/usr/bin/env python

from flask import Flask, request, jsonify
from whisper import start_whisper, transcribe
import os, uuid

start_whisper()

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    input_file = request.files['file']
    path = os.path.join("./input_files", input_file.filename)
    input_file.save(path)
    output = transcribe(path)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
