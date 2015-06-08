import pymysql as mdb
from secret import SQL_password

con = mdb.connect('localhost', 
	'root', 
	SQL_password,
	'tumblr_db'
	)