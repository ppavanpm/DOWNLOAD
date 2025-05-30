from flask import Flask, render_template, request, jsonify, send_file
from downloader import download_video, get_progress
import threading
import os
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
progress_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    quality = request.form['quality']
    uid = str(uuid.uuid4())
    progress_dict[uid] = {'status': 'Downloading...', 'progress': 0, 'filepath': None}

    def run_download():
        try:
            filepath = download_video(url, quality, uid, progress_dict)
            progress_dict[uid]['status'] = 'Done'
            progress_dict[uid]['filepath'] = filepath
        except Exception as e:
            progress_dict[uid]['status'] = f'Error: {str(e)}'

    threading.Thread(target=run_download).start()
    return jsonify({'id': uid})

@app.route('/progress/<id>')
def progress(id):
    return jsonify(progress_dict.get(id, {'status': 'Unknown'}))

@app.route('/download_file/<id>')
def download_file(id):
    file = progress_dict[id]['filepath']
    return send_file(file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
