d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def vocabulary(word):
  word = word.lower()
  try: 
    return d[word]
  except: 
    return "We couldn't find that word!"
 
word = input("Enter word: ")
print(vocabulary(word))

