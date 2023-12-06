import datetime

def greet_user():
    currentTime = datetime.datetime.now() 
    if currentTime.hour < 12:
        print("Good Morning!")
    else:
        print("Hello!")