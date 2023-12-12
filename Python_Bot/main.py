import asyncio
from helperFunctions import greetUser
from helperFunctions import news
from helperFunctions import playMusic
from helperFunctions import wiki
from helperFunctions import weather
from helperFunctions import joke
from helperFunctions import GPT
from helperFunctions import sendEmail

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

    #email = sendEmail.sendEmail('mihir17.udupa@gmail.com', 'Test Mail from JARVIS', 'Hai, This is a test email')

    readMail = sendEmail.readEmail()
    print("\n ---Emails--- \n", readMail)

    # url = playMusic.search_song('sea Shanty')
    # asyncio.run(playMusic.play_music(url, 'sea shanty'))

    # reply = GPT.askGPT('Write a simple code in python')
    # print(f"{reply}")

    # wikiResult = wiki.getwiki_content("ubuntu")
    # print(wikiResult)