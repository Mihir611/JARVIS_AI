import asyncio
import threading
import speech_recognition as sr
import pyttsx3
import time
from sqlite3 import Error
from datetime import date
from helperFunctions import greetUser
from helperFunctions import news
from helperFunctions import playMusic
from helperFunctions import wiki
from helperFunctions import weather
from helperFunctions import joke
from helperFunctions import GPT
from helperFunctions import sendEmail
from helperFunctions import bored
from helperFunctions import expenseTrack

# listener = sr.Recognizer()
# engine = pyttsx3.init()
# wake_word = "hey jarvis"

# def voice_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if wake_word in command:
#                 command = command.replace(wake_word, '')
#                 execute_command(command)
#     except:
#         pass

# def execute_command(command):
#     print(f"Received Command: {command}")

# def run_jarvis():
#     thread = threading.Thread(target=voice_command)
#     thread.start()

#     while True:
#         print("starting jarvis")
#         time.sleep(2)

# Main helpwer functions
def playMusic():
    url = playMusic.search_song('sea Shanty')
    asyncio.run(playMusic.play_music(url, 'sea shanty'))

def readEmails():
    readMail = sendEmail.readEmail()
    print("\n ---Emails--- \n", readMail)

def addExpense(connection):
    try:
        addingData = expenseTrack.add_expenses(connection, {
            'DATE': date.today() ,
            'TITLE': 'Hotel in Gokarna' ,
            'EXPENSE_TYPE': 'Debit',
            'AMOUNT': 5000,
            'OPENING_BALANCE': 0,
        })
    except:
        pass

def viewExpense(connection):
    try:
        expenseData = expenseTrack.view_expenses(connection)
        for row in expenseData:
            print(row)
    except Error as e:
        pass



if __name__ == "__main__":
    greeting = greetUser.greet_user()
    print(greeting)

    news = news.get_news()
    s = ' '.join(map(str, news))
    print("\n ---Today's News is as follows: ---\n"+ s)

    weatherData = weather.get_weather_report('Udupi')
    print("\n ---Weather Report--- \n",weatherData)

    laugh = joke.get_joke()
    print("\n ---Joke--- \n",laugh)

    advice = joke.advice()
    print("\n ---Advice--- \n",advice)

    thought = joke.thoughtOfDay()
    print("\n ---Thought--- \n", thought)

    # musicPlayback = threading.Thread(target=playMusic)

    # readMails = threading.Thread(target=readEmails)

    # musicPlayback.start()
    # readEmails.start()

    # musicPlayback.join()
    # readEmails.join()

    #email = sendEmail.sendEmail('mihir17.udupa@gmail.com', 'Test Mail from JARVIS', 'Hai, This is a test email')

    # reply = GPT.askGPT('Write a simple code in python')
    # print(f"{reply}")

    # wikiResult = wiki.getwiki_content("ubuntu")
    # print(wikiResult)


    # liking = input('What would you like to do ?\n')
    # if liking == 'options':
    #     options = input("Here are a few options\n1.Any Recreational Activity\n2.Activity with participents\n3.Random activity\n")

    #     match options:
    #         case 'Without participents':
    #             opts = input('Here are some available options to choose from\n 1.Education\n, 2.Recreational\n, 3.Social\n, 4.Diy\n, 5.Charity\n, 6.Cooking\n, 7.Relaxation\n, 8.Music\n, 9.Busywork\n')
    #             activityType = 'type='+opts
    #         case 'With participents':
    #             number = input('How many participents do you wish to have ?\n')
    #             activityType = 'participants='+number
    #         case 'random':
    #             activityType = ''
    #         case _:
    #             activityType = ''

    #     imBored = bored.imBored(activityType)
    #     print("\n ---Activity---\n",imBored)

    # else:
    #     print('Not able to uderstand you')


    # Expense Tracker Code
    try:
        connection = expenseTrack.connect()
        if connection is None:
            raise Error("Error connecting to database")  
    except Error as e:
        print(e)

    expenseTrackerOptions = int(input('Which operation do you want to perform? \n 1.Add Expense \n2.View Expense \n3.Get Monthly / Yearly report\n'))
    match expenseTrackerOptions:
        case 1:
            addExpense(connection)
        case 2:
           viewExpense(connection)
        case _:
            print('Not able to understand the option provided')

    # run_jarvis()