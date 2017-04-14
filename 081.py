names = ['Mercury', 'Venus', 'Moon', 'Chibi-Moon', 'Tuxedo Mask', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


while True:
  username = input("Enter a username:")
  # if we'd had a text file, we could have used this
  # with open('users.txt', r) as file:
  #   names = file.readlines()
  #   names.[i.strip("\n") for i in names]
    
  if username in names:
    print("Username is in use")
  else: 
    print("okay, good talk")
    break




while True:
  notes = []
  password = input("Enter new password:")

  if len(password) < 5:
    notes.append('must be at least 5 characters')
  if not any(i.isdigit() for i in password):
    notes.append('must have at least 1 number')
  if not any(i.isupper() for i in password):
    notes.append('must have at least 1 capital letter')
  if len(notes) == 0:
    print("Password is fine for you, I now dub thee " + username)
    break
  else:
    print("Please check the following:")  
    for n in notes: 
      print(n)