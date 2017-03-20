import string
import glob

list1 = []
files = glob.glob('letters/*.txt')

for file in files:
  with open(file, 'r') as file:
    letter = file.read().strip("\n")
    if letter in "python":
      list1.append(letter)

print(list1)