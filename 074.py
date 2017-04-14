import pandas
 
file1 = pandas.read_csv("./file1.txt")
file2 = pandas.read_csv("./file2.txt")
foo = [file1, file2]
# data_2.to_csv("sampledata_x_2.txt", index=None)
data = pandas.concat(foo)
data.to_csv("file3.txt", index=None)