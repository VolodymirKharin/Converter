from moviepy.editor import VideoFileClip
import wget
from datetime import datetime
from pathlib import Path
import os


class Mp4ToGif():
    raw_html = ''
    name_video_out = ''
    name_gif = ''
    html = ''

    def __init__(self, url):
        self.url = url


    def download_video(self):
        if not (Path("video").is_dir()):
            os.mkdir("video")
        self.name_video_out = f'video_{str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S"))}.mp4'
        print("Downloading video ....")
        wget.download(url=self.url, out=f'video\\{self.name_video_out}')
        print("Succesfull!")

    def convert_video_to_gif(self):
        if not (Path("gif").is_dir()):
            os.mkdir("gif")
        self.name_gif = f'gif{str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S"))}.gif'
        print("Converting video to gif ....")
        clip = VideoFileClip(f'video\\{self.name_video_out}')
        clip.write_gif(f'gif\\{self.name_gif}', fps=2)
        print("Succesfull!")

    def run_me(self):
        self.download_video()
        self.convert_video_to_gif()

