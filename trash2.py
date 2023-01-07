import eyed3
import urllib.request

import moviepy.editor as mp


# clip = mp.AudioFileClip(f"D:\Spotify Download\Black Balloons.mp4")
# clip.write_audiofile(f"D:\Spotify Download\Black Balloons.mp3")


audiofile = eyed3.load(f"D:\Spotify Download\Black Balloons.mp3")
audiofile.tag.artist = "artist_name_"
audiofile.tag.album = "album_name_"
audiofile.tag.title = "song_name_"

response = urllib.request.urlopen("https://i.scdn.co/image/ab67616d00001e02b6dbcf6fd8738a9460999453")
imagedata = response.read()
audiofile.tag.images.set(3, imagedata, "image/jpeg", u"cover")

audiofile.tag.save()