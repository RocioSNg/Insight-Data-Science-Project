#-----------------------------------------------------------#
#			Tumblr artist miner								#
#			Author: Rocio Ng								#
#			Purpose: Extract artist blog names 				#
#			from the Tumblr API by scraping posts			#
#			tagged 'artist on tumblr'						#
#-----------------------------------------------------------#

from API_functions import find_artists
from secret import SQL_password
import csv
import pymysql as mdb

print "Making calls to the Twitter API"
print "Starting to collect blog names from posts tagged 'artist on tumblr'"
artist_list = []

# collecected up to 1433326512
# 3600s in a hour
# 86400s in a day
# 604800s in a week
# 2592000 in 30 days (month)

# allow for calls to api to find artist at multiple time stamps:
time_stamp = 1433426522 # use latest time stamp
time_past = time_stamp - (6 * 2592000) # by month
increment = 3600/2 # half hour

# print find_artists(time_stamp)
while time_stamp > time_past:
 	print "Looking for artists posting at %i" % time_stamp
 	artist_list.extend(find_artists(time_stamp))
 	time_stamp -=  increment 

# update data base with artist names
# data base tumblr_db was created in mySQL

con = mdb.connect('localhost', 
	'root', 
	SQL_password,
	'tumblr_db'
	)



# print "Done! Now writing artists to file"


# # write list of artists to a csv file
# with open("tumblr_artists.txt", "w") as output:
#     writer = csv.writer(output, lineterminator=',')
#     for artist in artist_list:
#         writer.writerow([artist])    
