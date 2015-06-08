# from API_functions import *
# import json

# art = get_art("littleworries")

# get_art["short_url"]


import pymysql as mdb
from secret import SQL_password

con = mdb.connect('localhost', 'root', SQL_password, 'testdb') #host, user, password, #database

with con:
   cur = con.cursor()
   cur.execute("DROP TABLE IF EXISTS Writers")
   cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(25))")
   cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
   cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
   cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
   cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
   cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")

with con:
   cur = con.cursor()
   cur.execute("SELECT * FROM Writers")
   rows = cur.fetchall()
   for row in rows:
       print row