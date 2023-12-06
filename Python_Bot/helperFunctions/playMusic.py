import urllib.request
import re 
from pygame import mixer
import pytube
import asyncio

def search_song(song):
    query = urllib.parse.quote(song)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    video_ids = re.findall(r"watch\?v=(\S{11})", html.decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]

async def play_music(url):
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    
    print("Playing...")
    audio_file = stream.download()
    
    mixer.init()
    mixer.music.load(audio_file)
    mixer.music.play()
    
    while mixer.music.get_busy():
        await asyncio.sleep(1)
    
    mixer.quit()