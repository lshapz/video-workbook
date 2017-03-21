import string

foo = open('word3.txt', 'w')
for x in string.ascii_lowercase: 
  foo.write(x)
  foo.write('\n')

 
# with open("letters.txt", "w") as file:
#     for letter in string.ascii_lowercase:
#         file.write(letter + "\n")

