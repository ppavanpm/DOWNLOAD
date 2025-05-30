from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return render_template("index.html", error="Please enter a YouTube URL")

        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            temp_dir = tempfile.gettempdir()
            file_path = os.path.join(temp_dir, stream.default_filename)
            stream.download(output_path=temp_dir)

            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return render_template("index.html", error=f"Error: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
