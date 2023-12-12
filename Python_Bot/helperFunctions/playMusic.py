import urllib.request
import re 
from pygame import mixer
import pytube
import asyncio
import os
from moviepy.editor import *

def search_song(song):
    query = urllib.parse.quote(song)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    video_ids = re.findall(r"watch\?v=(\S{11})", html.decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]

async def play_music(url, song):
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file = stream.download()

    extCheck = os.path.splitext(audio_file)

    if extCheck[1] == ".mp4":
        FILETOCONVERT = AudioFileClip(audio_file)
        FILETOCONVERT.write_audiofile(f"{extCheck[0]}.mp3")
        FILETOCONVERT.close()

    print(f"Playing...{song}")
    audio_file = f"{extCheck[0]}.mp3"
    
    mixer.init()
    mixer.music.load(audio_file)
    mixer.music.play()
    
    while mixer.music.get_busy():
        await asyncio.sleep(1)
    
    mixer.quit()