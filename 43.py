import string

foo = string.ascii_lowercase[0::2]
bar = string.ascii_letters[1::2] 

with open('word4.txt', 'w') as file: 
  for i, j in zip(foo, bar):
    file.write(i + j + '\n')