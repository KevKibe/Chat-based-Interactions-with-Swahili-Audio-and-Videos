from pytube import YouTube
import os
import time

class YouTubeAudioDownloader:
    def __init__(self, url):
        self.url = url
        self.cwd = os.getcwd()
        self.yt = YouTube(self.url)
        self.audio_stream = self.yt.streams.filter(only_audio=True).first()
        self.filename = "audio.mp3"

    def download_audio(self):
        start_time = time.time()
        self.audio_stream.download(output_path=self.cwd, filename=self.filename)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Audio downloaded to {self.cwd}/{self.filename}")
        print(f"Elapsed time: {elapsed_time} seconds")