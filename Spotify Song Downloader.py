# Module dependecies for thies script are Spotipy,urllib,csv,Youtube_dl,re
# You can install these by running the following:-

# pip install spotipy
# pip install python-csv
# pip install urllib
# pip install regex
# pip install youtube_dl

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request
import re
import csv
import youtube_dl

# ----------------------------------------------------

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="------------------------------------", # Setup the spotify API and paste the Client ID and Secret here
                                               client_secret="----------------------------------"))

results = sp.playlist_items("3kRZgzHreNfUkqDaZe4r62") # Place your playlist ID or Playlist URL here 
total = results['total']

# ----------------------------------------------------

count = 0
index = 0
looprange = 0
totalrange= (total//100)+1

song =[]
song_name = []
links = []

# ----------------------------------------------------

def songs(index,count):
    temp = 100
    if totalrange-looprange==1:
        temp = total%100
    for i in range(temp):
        print(index,results['items'][count]['track']['name'],"by",results['items'][count]['track']['artists'][0]['name'])
        item1 = results['items'][count]['track']['name']+" by "+results['items'][count]['track']['artists'][0]['name']
        item2 = results['items'][count]['track']['name']
        song.append(item1)
        song_name.append(item2)
        count = count+1
        index = index+1
    count = 0

def download(dlink,file):
    video_url = dlink
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"D:\\Spotify Download\\"+file+".mp3"  # Your on destination path here
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

# ----------------------------------------------------

for i in range(totalrange):
    songs(index,count)
    index = index+100
    looprange = looprange+1
    results = sp.next(results)


with open('song.csv','w',encoding="utf_8") as o:
    writer = csv.writer(o)
    writer.writerow(song)
print("\n\n##################################################")
print("Songs lists Gathered!!")
print("\n##################################################")

# ----------------------------------------------------

for i in song:
    query = i
    org_query = urllib.parse.quote(query.replace(" ","+"))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+org_query)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_id = "https://www.youtube.com/watch?v="+video_ids[0]
    links.append(video_id)
    print(i,video_id)

with open('link.csv','w',encoding="utf_8") as o:
    writer = csv.writer(o)
    writer.writerow(links)
print("\n\n##################################################")
print("\nSong URLs Gathered!!")
print("\n##################################################")

# ----------------------------------------------------

print("\n\n---------------------------------------------------")
print("\nDownload Starting:- ")
print("\n---------------------------------------------------")
for i in range(len(links)):
    file = song_name[i]
    dlink = links[i]
    download(dlink,file)



