from flask import Flask, request, send_file, render_template
from downloader import download_youtube_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "No URL provided", 400
    
    try:
        filepath, title = download_youtube_video(url)
        response = send_file(filepath, as_attachment=True, download_name=f"{title}.mp4")

        @response.call_on_close
        def cleanup():
            import os
            try:
                os.remove(filepath)
            except Exception:
                pass

        return response
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
