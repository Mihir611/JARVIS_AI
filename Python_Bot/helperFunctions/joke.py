import requests
import random

def get_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def advice():
    res = requests.get('https://api.adviceslip.com/advice').json()
    return res['slip']['advice']

def thoughtOfDay():
    number = random.randint(0,15)
    res = requests.get("https://type.fit/api/quotes").json()
    thought = res[number]
    return thought
    