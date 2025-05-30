import yt_dlp
import os

def download_video(url):
    # Make sure 'downloads' folder exists
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'cookiefile': 'cookies.txt',  # Use the cookies you exported from your browser
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download completed successfully."
    except Exception as e:
        return f"Error: {str(e)}"
