import webbrowser
import subprocess

def play_music(query):
    search_term = query.replace("play","")
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.open(url)
    subprocess.call([])