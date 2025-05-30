from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from downloader import download_video
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            flash("Please enter a video URL")
            return redirect(url_for("index"))
        try:
            filepath = download_video(url)
            return send_file(filepath, as_attachment=True)
        except Exception as e:
            flash(str(e))
            return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
