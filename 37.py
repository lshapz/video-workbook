# Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.

def count(filepath):
  with open(filepath, 'r') as file:
    strng = file.read()
    print(len(strng.replace(",", " ").split()))

count('words2.txt')

# def count_words(filepath):
#     with open(filepath, 'r') as file:
#         strng = file.read()
#         strng_list = strng.split(" ")
#         return len(strng_list)
