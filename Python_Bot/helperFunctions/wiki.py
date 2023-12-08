import wikipedia

def getwiki_content(query):
    results = wikipedia.summary(query, sentences=2)
    return results