import requests
import json
from decouple import config

API_KEY = config('API')

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+API_KEY
    response = requests.get(url)
    data = json.loads(response.content)

    articles = []

    if data["status"] == "ok":
        for i in data['articles'][:5]:
            article = i["title"]
            articles.append(article)

    return articles
    