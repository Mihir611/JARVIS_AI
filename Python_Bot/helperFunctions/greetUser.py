from datetime import datetime
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def greet_user():
        hourData = datetime.now().hour

        if hourData >= 6 and hourData < 12:
            return "Good Morning " + USERNAME
        elif hourData >= 12 and hourData < 16:
            return "Good Afternoon " + USERNAME
        elif hourData >= 16 and hourData < 20:
            return "Good Evening " + USERNAME
        return "I'am "+ BOTNAME + ". How may i assist you ?"