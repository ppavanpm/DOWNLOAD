import yt_dlp
import uuid
import os

def download_video(url, quality="best"):
    temp_dir = "downloads"
    os.makedirs(temp_dir, exist_ok=True)

    filename = f"{uuid.uuid4()}.%(ext)s"
    output_path = os.path.join(temp_dir, filename)

    if quality == "audio":
        format_selector = "bestaudio"
    elif quality == "worst":
        format_selector = "worst"
    else:
        format_selector = "best"

    ydl_opts = {
        'format': format_selector,
        'outtmpl': output_path,
        'quiet': True,
        'noplaylist': True,
        'cookiefile': 'cookies.txt'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        final_path = ydl.prepare_filename(info)
        return final_path
