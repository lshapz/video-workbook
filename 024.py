d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# print(d.keys())

for x in d.items():
  print(str(x[0]) + " has value " + str(x[1]))
# 

for key, value in d.items():
  print(key + " has value " + str(value))