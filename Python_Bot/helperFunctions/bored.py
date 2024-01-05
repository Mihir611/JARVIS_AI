import requests

def imBored(command):
    if command == "":
        url = 'https://www.boredapi.com/api/activity'
    else:
        url = 'https://www.boredapi.com/api/activity?'+ command
    
    response = requests.get(url)
    return response.json()