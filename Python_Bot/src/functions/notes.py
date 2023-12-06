import pickle
import os
import datetime

notes = []

def get_fileName():
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S") + "-notes.txt"
    return filename

def takeNotes(text):
    notes.append(text)
    saveNotes()
    return "Note Saved"

def saveNotes():
    filename = get_fileName()
    with open(filename, "wb") as file:
        pickle.dump(notes, file)

def load_notes():
    filename = get_fileName()
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            notes = pickle.load(file)

def readNotes():
    pass