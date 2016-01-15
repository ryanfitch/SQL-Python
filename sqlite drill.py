# sqlite_drill.py by Ryan Fitch [http://ryan-fitch.com/]
# Python2
# tutorial drill from https://pythonprogramming.net/sql-database-python-part-1-inserting-database/
# Python: Putting data into a data base

import sqlite3
import time
import datetime

# connects you to the database
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# makes the table
def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def dataEntry():
    c.execute("INSERT INTO stuffToPlot VALUES(1, 1365952181,'2013-04-14 10:09:41','Python Sentiment',5)")
    c.execute("INSERT INTO stuffToPlot VALUES(2, 1365952257,'2013-04-14 10:10:57','Python Sentiment',6)")
    c.execute("INSERT INTO stuffToPlot VALUES(3, 1365952264,'2013-04-14 10:11:04','Python Sentiment',4)")
    conn.commit()

   
idfordb = 4
keyword = 'Python Sentiment'
value = 7

def dataEntry2():
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO stuffToPlot (ID, unix, datestamp, keyword, value) VALUES (?, ?, ?, ?, ?)",
              (idfordb, time.time(), date, keyword, value))
    conn.commit()
