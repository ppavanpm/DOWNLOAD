# app.py
from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            filename = stream.default_filename
            stream.download(output_path="downloads")
            return send_file(f"downloads/{filename}", as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    app.run(debug=True)
