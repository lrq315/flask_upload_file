import os
import uuid

from flask import Flask, request, render_template

BASE_DIR = '' # the folder where the file will be saved
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        file.save(os.path.join(BASE_DIR, filename))
        return 'File uploaded successfully'
    else:
        return 'No file selected'

if __name__ == '__main__':
    app.run()

