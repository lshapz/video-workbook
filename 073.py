import requests
import string
r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
text = r.text

with open('doubles.txt', 'w') as file:
  for i in text:
    if (i not in string.ascii_lowercase) & (i != ',') & (i != '\n'):
      i = str(int(i) * 2)
    file.write(i)


# import pandas
 
# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data_2 = data * 2
# data_2.to_csv("sampledata_x_2.txt", index=None)
