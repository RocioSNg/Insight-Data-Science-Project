from API_functions import get_art
import pandas as pd 
import json
import csv

# need to make sure art is NOT a REBLOG option is there

# extract artist user names from text file
with open('data/tumblr_artists_large.txt') as f:
	print "Now opening file containing list of artists"
	artist_list = list(csv.reader(f))[0]
print "%i artist names in file" % len(artist_list)

# get rid of duplicate artist:
artist_list = list(set(artist_list))
artist_list = filter(None, artist_list) # get rid of empty strings
artist_list.remove("sandersteins")
# print artist_list
print "There are %i artists in total" % len(artist_list)

# index artist list if short on time:
# artist_list = artist_list[0:3]
artists_artwork = {}


for blog_name in artist_list:
	print "now adding art for %s" % blog_name
	# artist = "angrygirlcomics"
	art_dump =  get_art(blog_name)
	art_dump = art_dump["posts"][0:20] # pulls out dictionary with info we want
	# print art_post

	for i in range(0,len(art_dump)):
		

		# print art_dump
		art_post = art_dump[i]
		tags = art_post["tags"]
		tags = [tag.encode('ascii', 'ignore') for tag in tags]
		
	
		artists_artwork[art_post["id"]] = [str(art_post["blog_name"]), str(art_post["date"]),
			tags]
# , str(art_post["note_count"])
print artists_artwork
	
df = pd.DataFrame.from_dict(artists_artwork, 'index')

df.columns = ['blog_name', 'date', 'tags']
print df
df.to_csv("artwork.csv")




# js = json.loads(art["posts"])
# print js[0:10]
# df = pd.DataFrame.from_dict(art)

# dat = json.load(art)
# df = pd.DataFrame(dat)