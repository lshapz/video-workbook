import requests
 
r = requests.get("http://www.pythonhow.com")
print(r.text[:100])


# rename local file to not overwrite import
# also pip install requests because I hadn't