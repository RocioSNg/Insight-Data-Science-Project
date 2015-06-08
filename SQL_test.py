import pymysql as mdb
from secret import SQL_password

con = mdb.connect('localhost', 
	'root', 
	SQL_password,
	'tumblr_db'
	)

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Artists")
	# cur.execute("CREATE TABLE Artists(Id INT PRIMARY KEY AUTO_INCREMENT,Blog_Name text not null)")
	# cur.execute("INSERT INTO Artists(Blog_Name) VALUES('crowdedteeth')")
	# cur.execute("INSERT INTO Artists(Blog_Name) VALUES('jeremyville')")

with con:
   cur = con.cursor()
   cur.execute("SELECT * FROM Artists")
   rows = cur.fetchall()
   for row in rows:
       print row