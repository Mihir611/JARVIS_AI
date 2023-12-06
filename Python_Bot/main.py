import asyncio
from helperFunctions import greetUser
from helperFunctions import news
from helperFunctions import playMusic

if __name__ == "__main__":
    greeting = greetUser.greet_user()
    print(greeting)

    news = news.get_news()
    s = ' '.join(map(str, news))
    print("Today's News is as follows:\n"+ s)

    url = playMusic.search_song('sea Shanty')
    asyncio.run(playMusic.play_music(url))

