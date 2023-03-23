from pytube import YouTube
from pytube import Search
from pytube.helpers import safe_filename 
import moviepy.editor as mp
import eyed3
import pandas as pd
import os
import urllib.request


base_path = "D:\\Songs\\V2\\Spotify Download\\" # Enter the Destination location here


songlist = pd.read_csv("songlist.csv")


queryname = songlist["queryname"].values.tolist()
song_name = songlist["song_name"].values.tolist()
artist_name = songlist["artist_name"].values.tolist()
album_name = songlist["album_name"].values.tolist()
thumbnail = songlist["thumbnail"].values.tolist()
links = songlist["links"].values.tolist()



error = []    

    
def download(links_,song_name_,artist_name_,album_name_,thumbnail_,count):
    video = YouTube(links_) 
    try:
        name = safe_filename(song_name_)
        file_already = os.listdir(path= base_path)
        if (name+".mp3") not in file_already:
            print(f'Downloading: {count} - {name} - {links_}')
            video.streams.get_audio_only().download(output_path=base_path,filename=name+".mp4")
            
            clip = mp.AudioFileClip(f"{base_path}{name}.mp4")
            clip.write_audiofile(f"{base_path}{name}.mp3")
            
            os.remove(f"{base_path}{name}.mp4")
            
            
            audiofile = eyed3.load(f"{base_path}{name}.mp3")
            audiofile.tag.artist = artist_name_
            audiofile.tag.album = album_name_
            audiofile.tag.title = song_name_
            
            response = urllib.request.urlopen(thumbnail_)
            imagedata = response.read()
            audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")
            
            audiofile.tag.save()
            
            if (name+".mp3") not in os.listdir(path= base_path):
                print("Error Happened")
                error.append({"Error":[song_name_,links_]})
                print({"Error":[song_name_,links_]})

        
        else:
            print(f"Already Exists - {count}")
            
    
        print("--------------------------")
        
    except Exception as e:
        print("**************************")
        print(e)
        error.append({"Error":[song_name_,links_]})
        print("Error Happened")
        print({"Error":[song_name_,links_]})
        
        print("**************************")
  
count = 1  
for i in range(songlist.shape[0]):
 
    song_name_ = song_name[i]
    artist_name_ = artist_name[i]
    album_name_ = album_name[i]
    thumbnail_ = thumbnail[i]
    links_ = links[i]
    
    download(links_,song_name_,artist_name_,album_name_,thumbnail_,count)
    count+=1

print(error)  



