import webbrowser

def search_google(query):
    search_term = query.replace("search", "")
    url = "https://www.google.com/search?q="+ search_term
    webbrowser.open(url)