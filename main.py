# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project 2

#This project is designed to build out some data frames using PANDAS

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


madeupdata = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

madeupdata = madeupdata.cumsum()

madeupdata.plot()

df = pd.DataFrame(
     np.random.randn(1000, 4), index=madeupdata.index, columns=["Plant 1", "Plant 2", "Plant 3", "Plant 4"]
        )

df = df.cumsum()

plt.figure()

df.plot()

plt.legend(loc='best')

plt.show()


