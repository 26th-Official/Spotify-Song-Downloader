import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="-----------------------", # Setup the spotify API and paste the Client ID and Secret here
                                               client_secret="-------------------------"))

results = sp.playlist_items("3kRZgzHreNfUkqDaZe4r62") # Place your playlist ID or Playlist URL here 
total = results['total']


with open("spotify.json","w") as f:
    json.dump(results,f)


count = 0
index = 0
looprange = 0
totalrange= (total//100)+1

queryname =[]

song_name = []
artist_name = []
album_name = []
links = []
thumbnail = []

# ----------------------------------------------------

def songs(index,count):
    temp = 100
    if totalrange-looprange==1:
        temp = total%100
    for i in range(temp):
        print(index,results['items'][count]['track']['name'],"by",results['items'][count]['track']['artists'][0]['name'])
        item1 = results['items'][count]['track']['name']+" by "+results['items'][count]['track']['artists'][0]['name']
        item2 = results['items'][count]['track']['name']
        item3 = results['items'][count]['track']['album']['images'][0]['url']
        item4 = results['items'][count]['track']['artists'][0]['name']
        item5 = results['items'][count]['track']['album']['name']
        
        
        queryname.append(item1)
        song_name.append(item2)
        thumbnail.append(item3)
        album_name.append(item5)
        artist_name.append(item4)
        
        count = count+1
        index = index+1
    count = 0
    
for i in range(totalrange):
    songs(index,count)
    index = index+100
    looprange = looprange+1
    results = sp.next(results)
    


queryname = pd.DataFrame(queryname,columns=["queryname"])
song_name = pd.DataFrame(song_name,columns=["song_name"])
artist_name = pd.DataFrame(artist_name,columns=["artist_name"])
album_name = pd.DataFrame(album_name,columns=["album_name"])
links = pd.DataFrame(links,columns=["links"])
thumbnail = pd.DataFrame(thumbnail,columns=["thumbnail"])

print("=================================================")
links = pd.read_csv("link.csv",index_col=False)
final = pd.concat([song_name,artist_name,album_name,thumbnail,links,queryname],axis=1)
print(final.head())
print("=================================================")
final.to_csv("songlist.csv",index=False)


