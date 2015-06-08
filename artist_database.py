# Extracts general information about artist blogs 
# using blog names extracted from API

from API_functions import Tumblr_Artist
import csv
import pandas as pd 

print "Making calls to the tumblr API"


# extract artist user names from text file
with open('data/tumblr_artists_large.txt') as f:
	print "Now opening file containing list of artists"
	artist_list = list(csv.reader(f))[0]
print "%i artist names in file" % len(artist_list)

# get rid of duplicate artist:
artist_list = list(set(artist_list))
artist_list = filter(None, artist_list) # get rid of empty strings
# print artist_list

# index artist list if short on time:

# artist_list = artist_list[0:500]


all_artists = {}

print "Now adding information about each blog"
print "There are %i artists in total" % len(artist_list)

for blog_name in artist_list:
	print "Adding info for user: %s" % blog_name
	artist = Tumblr_Artist(blog_name)
 	# print artist.blog_name
 	# print artist.blog_url()
 	# print artist.posts_count()
 	# artist_info = {artist.blog_name, 
 	# [artist.blog_url(), artist.posts_count()]}
 	all_artists[artist.blog_name] = [artist.blog_url(), 
 	artist.posts_count()]

print "Done! Now writing artists to file"

# print all_artists
df = pd.DataFrame.from_dict(all_artists, 'index')
print df
df.columns = ['url', 'posts_count']
df.to_csv("artist_info.csv")
# getting art from artist

# import urllib
# urllib.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")