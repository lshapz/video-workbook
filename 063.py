from time import sleep

i = 0 
while i < 5:
  if i == 4: 
    print("End of Loop")
  else:
    print("Hello")
    sleep(i)
  i += 1

# i = 0
# while True:
#   print("Hello")
#   i = i + 1
#   if i > 3:
#     print("End of Loop")
#     break
#   sleep(i)
