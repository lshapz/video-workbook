import requests
 
r = requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text

foo =text.count('a')
print(foo)
