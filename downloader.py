import yt_dlp
import os

COOKIE_FILE = "cookies.txt"  # Must be in the root folder

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'cookiefile': COOKIE_FILE,
        'quiet': True,
        'no_warnings': True,
    }

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filepath = ydl.prepare_filename(info_dict)
    return filepath
