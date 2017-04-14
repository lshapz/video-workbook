import string

big_string = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()?"


while True:

  password = input("Enter new password:")

  if len(password) >= 5 and any(i.isdigit() for i in password) and any(i.isupper() for i in password):
    print("okay")
    break
  else:
    print("Password is not fine")
  