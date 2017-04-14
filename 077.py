from datetime import datetime

age = input("")
year = datetime.now().year
old_year = year - int(age)
print("You were born back in " + str(old_year))
