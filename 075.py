import pandas
# import pylab as plt
import matplotlib.pyplot as plt


file1 = pandas.read_csv("./file1.txt")
file1.plot(x='x', y='x', kind='scatter')
plt.show()


