# from StringIO import StringIO
# f = open("words1.txt", "r")
# print(f.read())
# foo = str(f.read())
# print(foo)
# .split()
# print(foo)

with open("words1.txt") as file:
  my_data = file.read() 
  print(len(my_data.split()))


  
  
# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         strng = file.read()
#         strng_list = strng.split(" ")
#         return len(strng_list)
 
# print(count_words("words1.txt"))


