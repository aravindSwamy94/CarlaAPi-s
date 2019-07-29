import pandas as pd

data = pd.read_csv("waypoint.csv", delimiter = " ", header = None)

xdata = data.iloc[:, 0]
ydata = data.iloc[:, 1]

xlist = xdata.tolist()
ylist = ydata.tolist()

print(xlist)

print(ylist)

import matplotlib.pyplot as plt

plt.scatter(xlist, ylist)
plt.show()

