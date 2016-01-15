# sqlite_drill_3.py by Ryan Fitch [http://ryan-fitch.com/]
# Python2
# tutorial drill from https://pythonprogramming.net/sql-database-python-part-1-inserting-database/
# Python: Plotting from a SQL Database + Plotting with Dates

import sqlite3
import time
import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
wordUsed = 'Python Sentiment'
sql = "SELECT * FROM stuffToPlot WHERE keyword =?"

graphArray = []



for row in c.execute(sql, [(wordUsed)]):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    graphArrayAppend = splitInfo[2]+','+splitInfo[4]
    graphArray.append(graphArrayAppend)

datestamp, value = np.loadtxt(graphArray,delimiter=',', unpack=True,
                              converters={ 0: mdates.strpdate2num(' %Y-%m-%d %H:%M:%S')})

fig = plt.figure()

rect = fig.patch

ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=datestamp, y=value, fmt='b-', label = 'value', linewidth=4)
plt.show()   
	  
