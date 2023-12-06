import pickle
import os

todoList = []

def add_todo(item, fileName):
    global todoList
    todoList.append(item)
    save(fileName)
    return "Created the toDo list"

def readList():
    global todoList
    for item in todoList:
        return item
    
def save(file):
    with open(file, "wb") as f:
        for item in todoList:
            f.write(item + "\n")

def load(fileName):
    global todoList
    if os.path.exists(fileName):
        with open(fileName, "rb") as f:
            todoList = pickle.load(f)

def append(item, fileName):
    global todoList
    if os.path.exists(fileName):
        with open(fileName) as f:
            todoList.append(item)
                