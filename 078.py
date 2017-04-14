import random
import string 
# print(string.ascii_letters)
big_string = string.ascii_letters + string.digits + "!@#$%^&*()?"
big_list = list(big_string)

pass_string = ""

for x in range(0,6):
  pass_string += random.choice(big_list)

print(pass_string)
# his way: 
# chosen = random.sample(big_string, 6)
# pass_string = "".join(chosen)
