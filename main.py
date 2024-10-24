from yt_dlp import YoutubeDL


def download_yt_video(urls: list):
    save_path = 'videos/'
    ydl_opts = {
        'noplaylist': True,
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'format_sort': ['res', 'vcodec:h264', 'acodec:m4a']

    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == '__main__':
    URLS = ['https://www.youtube.com/watch?v=EYes5TtD26U&list=PLxdd3GbEcOtSIXnGL8NJTPdQy23uctuS9&index=7']
    download_yt_video(URLS)

