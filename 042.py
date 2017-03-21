a = [1, 2, 3]
b = (4, 5, 6)

zipped = zip(a, b)
  
for x in zipped:
  print(x[0] + x[1])



# for i, j in zip(a, b):
#   print(i + j)