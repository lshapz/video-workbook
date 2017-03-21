d = dict(weather = "clima", earth = "terra", rain = "chuva") 


def vocabulary(word):
  try: 
    trans = d[word]
  except: 
    trans = "We couldn't find that word!"
  return trans
 
word = input("Enter word: ")
print(vocabulary(word))

