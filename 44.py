import string

foo = string.ascii_lowercase[0::3]
bar = string.ascii_lowercase[1::3] 
baz = string.ascii_lowercase[2::3] + " "


with open('word5.txt', 'w') as file: 
  for i, j, k in zip(foo, bar, baz):
    file.write(i + j + k + '\n')