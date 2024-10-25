from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from yt_dlp import YoutubeDL
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

URLS = ['https://www.youtube.com/watch?v=EYes5TtD26U&list=PLxdd3GbEcOtSIXnGL8NJTPdQy23uctuS9&index=7']


def cut_video_parts(path: str, target_name):
    video_duration = VideoFileClip(path).duration
    first_part = {
        'file_name': '1.mp4',
        'start_time': 0,
        'end_time': 10
    }

    middle_part = {
        'file_name': '2.mp4',
        'start_time': video_duration / 2,
        'end_time': (video_duration / 2) + 10
    }

    last_part = {
        'file_name': '3.mp4',
        'start_time': video_duration - 10,
        'end_time': video_duration
    }

    ffmpeg_extract_subclip(path, first_part['start_time'], first_part['end_time'],
                           targetname=target_name + first_part['file_name'])
    ffmpeg_extract_subclip(path, middle_part['start_time'], middle_part['end_time'],
                           targetname=target_name+middle_part['file_name'])
    ffmpeg_extract_subclip(path, last_part['start_time'], last_part['end_time'],
                           targetname=target_name + last_part['file_name'])


def combine_shorts():
    short1 = VideoFileClip('shorts/short1.mp4')
    short2 = VideoFileClip('shorts/short2.mp4')
    short3 = VideoFileClip('shorts/short3.mp4')

    short1 = short1.set_audio(short1.audio)
    short2 = short2.set_audio(short2.audio)
    short3 = short3.set_audio(short3.audio)

    final_clip = concatenate_videoclips([short1, short2, short3])
    final_clip.write_videofile("shorts/my_concatenation.mp4", codec="libx264", audio_codec="aac")


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
    combine_shorts()
    # cut_video_parts('videos/Star Wars x Attack on Titan EPIC MASHUP ｜ Duel of The Fates x ətˈæk 0N tάɪtn.mp4',
    #                  'shorts/short')
    # download_yt_video(URLS)

