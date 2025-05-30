import yt_dlp
import os

def download_video(url, quality, uid, progress_dict):
    outtmpl = f"downloads/{uid}.%(ext)s"

    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '').strip()
            progress_dict[uid]['progress'] = percent
            progress_dict[uid]['status'] = f"Downloading: {percent}"
        elif d['status'] == 'finished':
            progress_dict[uid]['status'] = "Processing..."

    ydl_opts = {
        'outtmpl': outtmpl,
        'progress_hooks': [progress_hook],
    }

    if quality == 'audio':
        ydl_opts.update({
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })
    elif quality == 'low':
        ydl_opts['format'] = 'worst'
    else:
        ydl_opts['format'] = 'best'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = info.get('ext', 'mp4')
        return f"downloads/{uid}.{ext}"
