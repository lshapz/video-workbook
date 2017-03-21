import json

with open('company1.json', 'r') as file:
  print(json.load(file))

# from pprint import pprint
 
# with open("company1.json","r") as file:
#     d = json.loads(file.read())
 
# pprint(d)
