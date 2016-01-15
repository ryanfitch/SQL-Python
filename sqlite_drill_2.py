# sqlite_drill_2.py by Ryan Fitch [http://ryan-fitch.com/]
# Python2
# tutorial drill from https://pythonprogramming.net/sql-database-python-part-1-inserting-database/
# Python: Reading data from a data base


import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
sql = "SELECT * FROM stuffToPlot WHERE keyword =?"

wordUsed = 'Python Sentiment'

def readData():
    for row in c.execute(sql, [(wordUsed)]):
        print row
        # print str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    

readData()
