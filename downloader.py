from pytube import YouTube
import os
import re

def sanitize_filename(name):
    # Remove invalid filename chars
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_youtube_video(url):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not stream:
        raise Exception("No suitable video streams found")

    title = sanitize_filename(yt.title)
    filename = "temp_video.mp4"
    stream.download(filename=filename)

    return filename, title
