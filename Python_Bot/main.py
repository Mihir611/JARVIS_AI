import asyncio
from helperFunctions import greetUser
from helperFunctions import news
from helperFunctions import playMusic
from helperFunctions import wiki
from helperFunctions import weather
from helperFunctions import joke

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

    # url = playMusic.search_song('sea Shanty')
    # asyncio.run(playMusic.play_music(url))

    # wikiResult = wiki.getwiki_content("ubuntu")
    # print(wikiResult)