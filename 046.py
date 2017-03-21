

import string
import glob

list1 = []
files = glob.glob('letters/*.txt')

for file in files:
  with open(file, 'r') as file:
    list1.append(file.read().strip("\n"))


# list1 = []
# with os.listdir('letters') as files:
#   for x in files:
#     f = open(x + '.txt', 'r')
#     list1.append(f.read())


print(list1)
