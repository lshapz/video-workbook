import string

big_string = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()?"

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
    print("Password is fine")
    break
  else:
    print("Please check the following:")  
    for n in notes: 
      print(n)