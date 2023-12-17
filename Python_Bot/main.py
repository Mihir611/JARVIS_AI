import asyncio
import threading
import speech_recognition as sr
import pyttsx3
import time
from helperFunctions import greetUser
from helperFunctions import news
from helperFunctions import playMusic
from helperFunctions import wiki
from helperFunctions import weather
from helperFunctions import joke
from helperFunctions import GPT
from helperFunctions import sendEmail

listener = sr.Recognizer()
engine = pyttsx3.init()
wake_word = "hey jarvis"

def voice_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if wake_word in command:
                command = command.replace(wake_word, '')
                execute_command(command)
    except:
        pass

def execute_command(command):
    print(f"Received Command: {command}")

def run_jarvis():
    thread = threading.Thread(target=voice_command)
    thread.start()

    while True:
        print("starting jarvis")
        time.sleep(2)

def playMusic():
    url = playMusic.search_song('sea Shanty')
    asyncio.run(playMusic.play_music(url, 'sea shanty'))

def readEmails():
    readMail = sendEmail.readEmail()
    print("\n ---Emails--- \n", readMail)

if __name__ == "__main__":
    # greeting = greetUser.greet_user()
    # print(greeting)

    # news = news.get_news()
    # s = ' '.join(map(str, news))
    # print("\n ---Today's News is as follows: ---\n"+ s)

    # weatherData = weather.get_weather_report('Udupi')
    # print("\n ---Weather Report--- \n",weatherData)

    # laugh = joke.get_joke()
    # print("\n ---Joke--- \n",laugh)

    # advice = joke.advice()
    # print("\n ---Advice--- \n",advice)

    # thought = joke.thoughtOfDay()
    # print("\n ---Thought--- \n", thought)

    # musicPlayback = threading.Thread(target=playMusic)

    # readMails = threading.Thread(target=readEmails)

    # musicPlayback.start()
    # readEmails.start()

    # musicPlayback.join()
    # readEmails.join()

    # #email = sendEmail.sendEmail('mihir17.udupa@gmail.com', 'Test Mail from JARVIS', 'Hai, This is a test email')

    # # reply = GPT.askGPT('Write a simple code in python')
    # # print(f"{reply}")

    # # wikiResult = wiki.getwiki_content("ubuntu")
    # # print(wikiResult)

    run_jarvis()