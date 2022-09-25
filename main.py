# INF601 - Advanced Programming in Python
# Jesse Heckman
# Mini Project 2

#This project is designed to build out some data frames using PANDAS

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Using the example for made up data with numpy. Could not get CSV data to load with values.
# Continue to explore data imports, specifically how to get .csv to load correctly.
# Here is an example of the data that I could not import. Column headers and name would import but numbers did not.

# Takes the file's folder
#filepath = r"C:\Users\JLHEC\Downloads\2018_Cyanotoxins_Chl_Genetics_Data.csv"

# read the CSV file
#df = pd.read_csv(filepath)

# print the first five rows
#print(df.head())


# Make up some random data and store as variable madeupdata

madeupdata = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

# Move made up data into a pandas data frame for use. Make up labels for the data columns

df = pd.DataFrame(
     np.random.randn(1000, 4), index=madeupdata.index, columns=["Plant 1", "Plant 2", "Plant 3", "Plant 4"]
        )

df = df.cumsum()

plt.figure()
# Plot the made up data in pandas data frame
df.plot()

plt.legend(loc='best')

# Save the plotted data in charts file
plt.savefig('charts/madeupdata.png')

#Show the data in pycharm
plt.show()


