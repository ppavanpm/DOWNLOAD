from flask import Flask, render_template, request, send_file, redirect, flash
from downloader import download_video
import os

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        quality = request.form.get('quality', 'best')
        try:
            filepath = download_video(url, quality)
            return send_file(filepath, as_attachment=True)
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
