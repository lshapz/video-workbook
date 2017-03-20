import string
import os

os.makedirs('letters')

for x in string.ascii_lowercase:
  with open("letters/" + x + '.txt', 'w') as file:
    file.write(x + '\n')