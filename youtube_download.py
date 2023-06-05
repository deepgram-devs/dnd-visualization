import youtube_dl

def download_audios(vids, directory):
    output = directory + '/%(title)s.mp3'
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # change this to change where you download it to
    'outtmpl': output,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(vids)
