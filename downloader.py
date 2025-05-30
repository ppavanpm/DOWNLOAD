import yt_dlp
import os
import re

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_youtube_video(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'temp_video.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = sanitize_filename(info_dict.get('title', 'video'))
        ext = info_dict.get('ext', 'mp4')
        filename = f"temp_video.{ext}"
    return filename, title
