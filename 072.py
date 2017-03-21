import webbrowser

search_term = input("Enter your Google query: ") 
url = "http://google.com/search?q=" + search_term

webbrowser.open_new(url)