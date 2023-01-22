from moviepy.editor import *
from pathlib import Path

videoclip = Path('videoclip.mp4')

video = VideoFileClip(f'{videoclip}')
audio = video.audio
audio.write_audiofile(f'{videoclip.stem}.mp3')